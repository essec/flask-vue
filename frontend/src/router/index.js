import Vue from 'vue'
import Router from 'vue-router'


const routerOption = [
  { path: '/', component: 'Home', name: 'Home'},
  { path: '/about', component: 'About', name: 'About'},
  { path: '/hello', component: 'HelloWorld', name: 'Hello'},
  { path: '/books', component: 'Books', name: 'Books'},
  { path: '*', component: 'NotFound' },
  { path:'/ping', component: 'Ping', name:'Ping'},
  { path: '/test', component: 'test' }
]

const routes = routerOption.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode : 'history'
})
