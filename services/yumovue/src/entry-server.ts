import { renderToString } from "vue/server-renderer";
import { createApp } from "./main"


// export const render = async () => {
//   const { app, router, pinia} = createApp()

// }
export async function render(_url:string){
  const { app, router, pinia } = createApp()

  // 注册路由
  router.push(_url)
  await router.isReady()

  // 注入 vue ssr中的上下文对象
  const ctx: {modules?: string[]} = {}
  const html = await renderToString(app, ctx)

  return [html, JSON.stringify(pinia.state.value)]
}
