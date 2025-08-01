import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import express from "express"
import { createServer as createViteServer } from 'vite'


const __dirname = path.dirname(fileURLToPath(import.meta.url))

async function createServer() {
  const app = express()

  /**
   * @官方解释
   * 以中间件模式创建vite应用，这将禁用vite自身的HTML服务逻辑
   * 并让上级服务器接管
   */ // 创建vite服务
  const vite = await createViteServer({
    server: {
      middlewareMode: true
    },
    root: process.cwd(),
    logLevel: "error",
    appType: 'custom'
  })

  // 注册vite的Connect实例作为中间件 ·（注意：vite.middlewares 是一个 Connect 实例）
  app.use(vite.middlewares)

  app.use("*all", async (req, res, next) =>{
    const url = req.originalUrl

    try {
      // 读取index.html
      let template = fs.readFileSync(
        path.resolve(__dirname, "index.html"),
        "utf-8"
      )
      // 应用vite html 转换， 注入vite HMR
      template = await vite.transformIndexHtml(url, template)

      // 加载服务端入口, vite.ssrLoadModule将自动转换
      const { render } = await vite.ssrLoadModule("/src/entry-server.ts")

      // 渲染应用的html
      const [appHtml, piniaState] = await render(url)
      const html = template
        .replace("<!--ssr-outlet-->", () => appHtml)  // 替换处理后的模板
        .replace("<!--pinia-state-->", piniaState)    // 注入pinia state


      res.status(200).set({"content-type": "text/html"}).end(html)
    } catch(err) {
      vite?.ssrFixStacktrace(err)
      next(err)
    }
  })
  app.listen(8080)
}

createServer()
