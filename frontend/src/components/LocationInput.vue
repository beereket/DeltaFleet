<template>
  <div class="inputs">
    <label>Origin:</label>
    <gmap-autocomplete @place_changed="setOrigin" />

    <label>Destination:</label>
    <gmap-autocomplete @place_changed="setDestination" />

    <div v-for="(wp, index) in waypointFields" :key="index">
      <label>Stop {{ index + 1 }}:</label>
      <gmap-autocomplete @place_changed="place => setWaypoint(place, index)" />
    </div>

    <button @click="addWaypoint">+ Add Stop</button>
    <button v-if="waypointFields.length" @click="removeWaypoint">− Remove Last Stop</button>
  </div>
</template>

<script>
export default {
  props: ['onOriginChange', 'onDestinationChange', 'onWaypointsChange'],
  data() {
    return {
      waypointFields: [],
      waypoints: []
    };
  },
  methods: {
    setOrigin(place) {
      if (!place.geometry) return;
      const loc = place.geometry.location;
      this.onOriginChange({ lat: loc.lat(), lng: loc.lng() });
    },
    setDestination(place) {
      if (!place.geometry) return;
      const loc = place.geometry.location;
      this.onDestinationChange({ lat: loc.lat(), lng: loc.lng() });
    },
    addWaypoint() {
      this.waypointFields.push({});
      this.waypoints.push(null);
    },
    removeWaypoint() {
      this.waypointFields.pop();
      this.waypoints.pop();
      this.emitWaypoints();
    },
    setWaypoint(place, index) {
      if (!place.geometry) return;
      const loc = place.geometry.location;
      this.$set(this.waypoints, index, {
        location: { lat: loc.lat(), lng: loc.lng() }
      });
      this.emitWaypoints();
    },
    emitWaypoints() {
      const valid = this.waypoints.filter(
          wp => wp?.location?.lat !== undefined && wp?.location?.lng !== undefined
      );
      this.onWaypointsChange(valid);
    }
  }
}
</script>

<style scoped>
.inputs {
  margin-bottom: 20px;
}
gmap-autocomplete {
  display: block;
  margin-bottom: 10px;
  width: 100%;
}
button {
  margin: 5px;
}
</style>
