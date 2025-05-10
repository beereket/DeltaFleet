import Vue from 'vue'
import Router from 'vue-router'
import RegisterView from "@/views/auth/RegisterView.vue";
import LoginView from "@/views/auth/LoginView.vue";
import UnAuthorized from "@/views/common/UnAuthorized.vue";
import NotFound from "@/views/common/NotFound.vue";
import Setup2FA from "@/views/twoFA/Setup2FA.vue";
import Disable2FA from "@/views/twoFA/Disable2FA.vue";
import VerifyEmail from "@/components/auth/VerifyEmail.vue";
import CheckEmail from "@/components/auth/CheckEmail.vue";

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        // Auth
        { path: '/register', name: 'Register', component: RegisterView},
        { path: '/login', name: 'Login', component: LoginView},
        {
            path: '/verify-email/:uidb64/:token/',
            component: VerifyEmail,
            name: 'verify-email'
        },
        {
            path: '/check-email',
            component: CheckEmail,
            name: 'check-email'
        },

        // TwoFA
        { path: '/2fa-setup', component: Setup2FA },
        { path: '/2fa-disable', component: Disable2FA },

        // Admin

        // Manager
        { path: '/manager/trips/create', component: () => import('@/views/manager/CreateTrip.vue')},
        // Driver

        // Common
        { path: '/profile', component: () => import('@/views/common/ProfileView.vue') },
        { path: '/unauthorized', component: UnAuthorized },
        { path: '*', component: NotFound },
        { path: '/map', component: () => import('@/views/common/MapView.vue')}
    ]
})
