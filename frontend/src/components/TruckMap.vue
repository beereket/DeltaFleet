<template>
  <div style="position: relative">
    <!-- Google Map -->
    <GmapMap
        ref="gmapRef"
        :center="mapCenter"
        :zoom="7"
        style="width: 100%; height: 500px"
    >
      <!-- Origin Marker -->
      <GmapMarker
          v-if="origin"
          :position="origin"
          :icon="truckIcon"
          label="A"
          @click="openInfo('origin')"
      />
      <GmapInfoWindow
          v-if="infoWindow === 'origin'"
          :position="origin"
          @closeclick="infoWindow = null"
      >
        <div><strong>🅰 Origin</strong></div>
      </GmapInfoWindow>

      <!-- Destination Marker -->
      <GmapMarker
          v-if="destination"
          :position="destination"
          :icon="truckIcon"
          label="B"
          @click="openInfo('destination')"
      />
      <GmapInfoWindow
          v-if="infoWindow === 'destination'"
          :position="destination"
          @closeclick="infoWindow = null"
      >
        <div><strong>🅱 Destination</strong></div>
      </GmapInfoWindow>

      <!-- Waypoints -->
      <GmapMarker
          v-for="(stop, index) in safeWaypoints"
          :key="index"
          :position="stop.location"
          :icon="truckIcon"
          :label="String(index + 1)"
          @click="openInfo('stop-' + index)"
      />
      <GmapInfoWindow
          v-for="(stop, index) in safeWaypoints"
          :key="'info-' + index"
          v-if="infoWindow === ('stop-' + index)"
          :position="stop.location"
          @closeclick="infoWindow = null"
      >
        <div><strong>📍 Stop {{ index + 1 }}</strong></div>
      </GmapInfoWindow>

      <!-- Route -->
      <GmapDirectionsRenderer
          v-if="directions"
          :directions="directions"
      />
    </GmapMap>

    <!-- Overlay until route is ready -->
    <div v-if="!isRouteReady" class="map-overlay">
      📍 Select origin and destination to view the route.
    </div>

    <!-- Route summary -->
    <div v-if="tripSummary" class="info">
      <p><strong>Distance:</strong> {{ tripSummary.distance }}</p>
      <p><strong>Duration:</strong> {{ tripSummary.duration }}</p>
    </div>

    <!-- Export button -->
    <button v-if="directions" @click="exportRoute" class="export-btn">
      📦 Export Route as JSON
    </button>

    <!-- Sidebar summary -->
    <div v-if="routeStops.length" class="sidebar">
      <h3>📍 Route Stops</h3>
      <ul>
        <li v-for="(stop, i) in routeStops" :key="i">
          <strong>{{ stop.label }}:</strong> {{ stop.start }} → {{ stop.end }}<br />
          🕓 {{ stop.duration }} | 📏 {{ stop.distance }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import GmapDirectionsRenderer from './GmapDirectionsRenderer.vue'

export default {
  components: { GmapDirectionsRenderer },
  props: {
    origin: Object,
    destination: Object,
    waypoints: {
      type: Array,
      default: () => [],
    }
  },
  data() {
    return {
      defaultCenter: { lat: 43.238949, lng: 76.889709 },
      directions: null,
      tripSummary: null,
      infoWindow: null,
      truckIcon: {
        url: 'https://cdn-icons-png.flaticon.com/512/1070/1070798.png',
        scaledSize: new google.maps.Size(40, 40),
      },
    };
  },
  computed: {
    mapCenter() {
      return this.origin?.lat && this.origin?.lng ? this.origin : this.defaultCenter;
    },
    safeWaypoints() {
      return this.waypoints.filter(
          wp => wp?.location?.lat !== undefined && wp?.location?.lng !== undefined
      );
    },
    isRouteReady() {
      return this.origin && this.destination && this.directions;
    },
    routeStops() {
      if (!this.directions || !this.directions.routes.length) return [];
      const legs = this.directions.routes[0].legs;
      return legs.map((leg, index) => ({
        label:
            index === 0 ? 'Start' :
                index === legs.length - 1 ? 'Finish' :
                    `Stop ${index}`,
        start: leg.start_address,
        end: leg.end_address,
        distance: leg.distance.text,
        duration: leg.duration.text
      }));
    }
  },
  watch: {
    origin: 'drawRoute',
    destination: 'drawRoute',
    waypoints: {
      handler: 'drawRoute',
      deep: true,
    },
  },
  methods: {
    openInfo(id) {
      this.infoWindow = id;
    },
    drawRoute() {
      if (!this.origin || !this.destination) return;

      const service = new google.maps.DirectionsService();
      service.route(
          {
            origin: this.origin,
            destination: this.destination,
            waypoints: this.safeWaypoints,
            travelMode: 'DRIVING',
            optimizeWaypoints: true,
          },
          (result, status) => {
            if (status === 'OK') {
              this.directions = result;

              const legs = result.routes[0].legs;
              let distance = 0, duration = 0;
              legs.forEach(l => {
                distance += l.distance.value;
                duration += l.duration.value;
              });

              this.tripSummary = {
                distance: (distance / 1000).toFixed(1) + ' km',
                duration: Math.floor(duration / 60) + ' min',
              };

              const bounds = new google.maps.LatLngBounds();
              result.routes[0].overview_path.forEach(p => bounds.extend(p));
              this.$refs.gmapRef.$mapObject.fitBounds(bounds);
            } else {
              console.error('Route error:', status);
              this.directions = null;
              this.tripSummary = null;
            }
          }
      );
    },
    exportRoute() {
      const route = this.directions.routes[0];
      const legs = route.legs;
      const waypoints = [];

      for (let i = 0; i < legs.length; i++) {
        if (i !== 0) {
          waypoints.push({
            lat: legs[i].start_location.lat(),
            lng: legs[i].start_location.lng(),
            address: legs[i].start_address
          });
        }
      }

      const routeData = {
        origin: {
          lat: legs[0].start_location.lat(),
          lng: legs[0].start_location.lng(),
          address: legs[0].start_address
        },
        destination: {
          lat: legs[legs.length - 1].end_location.lat(),
          lng: legs[legs.length - 1].end_location.lng(),
          address: legs[legs.length - 1].end_address
        },
        waypoints: waypoints,
        total_distance: this.tripSummary.distance,
        total_duration: this.tripSummary.duration
      };

      const blob = new Blob([JSON.stringify(routeData, null, 2)], {
        type: 'application/json'
      });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'truck_route.json';
      link.click();
      URL.revokeObjectURL(url);
    }
  }
}
</script>

<style scoped>
.map-overlay {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(255, 255, 255, 0.9);
  padding: 20px 30px;
  border-radius: 10px;
  font-size: 18px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  z-index: 10;
  text-align: center;
  pointer-events: none;
}
.info {
  background: #f4f4f4;
  padding: 10px;
  margin-top: 10px;
}
.export-btn {
  margin-top: 10px;
  padding: 8px 14px;
  background-color: #2e86de;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.sidebar {
  background: #f9f9f9;
  padding: 15px;
  border-radius: 6px;
  margin-top: 20px;
}
.sidebar h3 {
  margin-bottom: 10px;
}
.sidebar ul {
  list-style: none;
  padding-left: 0;
}
.sidebar li {
  margin-bottom: 12px;
  line-height: 1.4;
}
</style>
