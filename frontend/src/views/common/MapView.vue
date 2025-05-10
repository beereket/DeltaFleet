<template>
  <div id="app" style="display: flex">
    <!-- Left panel -->
    <div style="flex: 1">
      <LocationInput
          :onOriginChange="o => origin = o"
          :onDestinationChange="d => destination = d"
          :onWaypointsChange="w => waypoints = w"
      />
      <input type="file" accept=".json" @change="importRoute" />
      <button @click="saveCurrentRoute" :disabled="!origin || !destination">💾 Save This Route</button>
      <TruckMap :origin="origin" :destination="destination" :waypoints="waypoints" />
    </div>

    <!-- Right saved routes list -->
    <div style="width: 300px; padding: 10px; border-left: 1px solid #ccc">
      <h3>📂 Saved Routes</h3>
      <ul>
        <li
            v-for="(route, index) in savedRoutes"
            :key="index"
            @click="loadSavedRoute(route)"
            style="cursor: pointer; margin-bottom: 8px"
        >
          📍 {{ route.origin.address }} → {{ route.destination.address }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import LocationInput from '@/components/LocationInput.vue'
import TruckMap from '@/components/TruckMap.vue'

export default {
  components: { LocationInput, TruckMap },
  data() {
    return {
      origin: null,
      destination: null,
      waypoints: [],
      savedRoutes: []
    }
  },
  mounted() {
    this.loadAllRoutes();
  },
  methods: {
    importRoute(event) {
      const file = event.target.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const json = JSON.parse(e.target.result);
          this.origin = {
            lat: json.origin.lat,
            lng: json.origin.lng
          };
          this.destination = {
            lat: json.destination.lat,
            lng: json.destination.lng
          };
          this.waypoints = json.waypoints.map(wp => ({
            location: { lat: wp.lat, lng: wp.lng }
          }));
        } catch (err) {
          alert('❌ Invalid JSON');
          console.error(err);
        }
      };
      reader.readAsText(file);
    },
    saveCurrentRoute() {
      if (!this.origin || !this.destination) return;

      const routeData = {
        origin: { ...this.origin, address: 'Origin' },
        destination: { ...this.destination, address: 'Destination' },
        waypoints: this.waypoints
      };

      // Optionally add address labels if available from directions
      const key = Date.now();
      localStorage.setItem(`route-${key}`, JSON.stringify(routeData));
      this.loadAllRoutes();
    },
    loadAllRoutes() {
      this.savedRoutes = [];
      Object.keys(localStorage)
          .filter(k => k.startsWith('route-'))
          .forEach(k => {
            try {
              const route = JSON.parse(localStorage.getItem(k));
              this.savedRoutes.push(route);
            } catch {}
          });
    },
    loadSavedRoute(route) {
      this.origin = {
        lat: route.origin.lat,
        lng: route.origin.lng
      };
      this.destination = {
        lat: route.destination.lat,
        lng: route.destination.lng
      };
      this.waypoints = route.waypoints || [];
    }
  }
}

</script>