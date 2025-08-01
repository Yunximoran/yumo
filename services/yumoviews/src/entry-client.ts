import { createApp } from "./main"




// 创建应用实例
const {app, router, pinia} = createApp()

router.isReady().then(()=>{
  if (window.__INITIAL_STATE__) {
    pinia.state.value = JSON.parse(window.__INITIAL_STATE__)
  }
  app.mount("#app")
})
