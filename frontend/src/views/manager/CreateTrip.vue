<template>
  <div id="app">
    <h2>Create Trip 🛣️</h2>
    <LocationInput
        :onOriginChange="setOrigin"
        :onDestinationChange="setDestination"
    />
    <TruckMap
        v-if="origin && destination"
        :origin="origin"
        :destination="destination"
    />
  </div>
</template>

<script>
import LocationInput from '@/components/LocationInput.vue'
import TruckMap from '@/components/TruckMap.vue'

export default {
  name: 'CreateTrip',
  components: { LocationInput, TruckMap },
  data() {
    return {
      origin: null,
      destination: null,
    }
  },
  methods: {
    setOrigin(location) {
      console.log('Setting origin:', location);
      this.origin = location;
    },
    setDestination(location) {
      console.log('Setting destination:', location);
      this.destination = location;
    }
  }
}
</script>

<style scoped>
#app {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

h2 {
  color: #333;
  margin-bottom: 20px;
  font-size: 24px;
}
</style>
