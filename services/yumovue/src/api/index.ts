import axios, {
  type AxiosInstance,
  AxiosError,
  type AxiosRequestConfig,
  type AxiosResponse,
  Axios
} from 'axios'


import { ElMessage } from 'element-plus'
import { type ResultData } from './index.data'


const baseURL:string = import.meta.env.VITE_API_BASEURL


enum RequestEnums {
  TIMEOUT = 20000,
  OVERDUE = 401,
  FAIL = 400,
  SUCCESS = 200
}


const config = {
  baseURL,
  timeout: RequestEnums.TIMEOUT as number,
  withCredentials: true,
}


class RequestHttp  {
  service: AxiosInstance
  public constructor(config: AxiosRequestConfig) {
    // 实例化axios
    this.service = axios.create(config)

    /**
     * 请求拦截器
     * 客户端发送请求 -> [请求拦截器] -> 服务器
     * token校验(JWT) : 接受服务器返回的token,存储到vuex/pinia/本地储存当中
    */
    this.service.interceptors.request.use(
      (config: any) => {
        return {
          ...config
        }
      },
      (error: AxiosError) => {
        Promise.reject(error)
      }
    )

    /**
     * 响应拦截器
     * 服务器换返回信息 -> [拦截统一处理] -> 客户端JS获取到信息
    */
    this.service.interceptors.response.use(
      (response: AxiosResponse) => {
        const {data} = response
        if (data.code === RequestEnums.OVERDUE) {
          return Promise.reject(data)
        }
        if (data.code && data.code !== RequestEnums.SUCCESS) {
          ElMessage.error(data.msg)
          return Promise.reject(data)
        }
        return data
      },
      (error: AxiosError) => {
        const { response } = error
        if (response) {
          this.handleCode(response.status)
        }

        if (!window.navigator.onLine) {
          ElMessage.error("网络连接失败")
        }
      }
    )
  }
  handleCode(code: number): void {
    switch(code) {
      case 401:
        ElMessage.error("登录失败，请重新登录")
        break
      default:
        ElMessage.error("请求失败")
        break
    }
  }
}


export default new RequestHttp(config)
