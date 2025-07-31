import './assets/main.css'
import { createSSRApp } from 'vue'
import App from '@/App.vue'


import router from '@/router'
import requests from "@/requests"
import pinia from "@/stores"



// 导出ssr app实例
export function createApp() {
  const app = createSSRApp(App)
  app.config.globalProperties.$requests = requests
  app.use(pinia)
  app.use(router)

  return { app, pinia, router}
}



