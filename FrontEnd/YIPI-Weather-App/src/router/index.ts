import { createRouter, createWebHistory } from 'vue-router'
import SplashScreenView from '../views/SplashScreen.vue'
// import TriviaView from '../views/Trivia.vue'
// import ClimateView from '../views/Climate.vue'
// import ProfileView from '../views/Profile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'splash screen',
      component: SplashScreenView,
    },
    // {
    //   path: '/trivia',
    //   name: 'trivia',
    //   component: TriviaView,
    // },
    // {
    //   path: '/climate',
    //   name: 'climate',
    //   component: ClimateView,
    // },
    // {
    //   path: '/profile',
    //   name: 'profile',
    //   component: ProfileView,
    // },
  ],
})

export default router