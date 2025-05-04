import Vue from 'vue'
import Router from 'vue-router'
import RegisterView from "@/views/auth/RegisterView.vue";
import LoginView from "@/views/auth/LoginView.vue";

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/register',
            name: 'Register',
            component: RegisterView
        },
        {
            path: '/login',
            name: 'Login',
            component: LoginView
        }
    ]
})
