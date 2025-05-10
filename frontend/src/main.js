import Vue from 'vue'
import App from './App.vue'
import router from './router'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDkK-aPpEdhOcfU6tVtF-n05BcFX7oOyrY',
    libraries: 'places',
  },
  installComponents: true,
})
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
