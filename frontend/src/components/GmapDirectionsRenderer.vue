<template>
  <div></div>
</template>

<script>
export default {
  name: 'GmapDirectionsRenderer',
  props: {
    directions: { type: Object, required: true }
  },
  data() {
    return {
      renderer: null
    }
  },
  mounted() {
    this.renderer = new google.maps.DirectionsRenderer();
    this.renderer.setMap(this.$parent.$mapObject);
    this.renderer.setDirections(this.directions);
  },
  watch: {
    directions(newVal) {
      if (this.renderer && newVal) {
        this.renderer.setDirections(newVal);
      }
    }
  },
  destroyed() {
    if (this.renderer) {
      this.renderer.setMap(null);
    }
  }
}
</script>
