import axios, {
  type AxiosInstance,
  type AxiosRequestConfig,
  type InternalAxiosRequestConfig,
  type AxiosResponse,
  AxiosError
} from "axios"

import { ElMessage } from "element-plus"


// 数据返回接口
interface Result {
  code: number
  msg: string
}

// 请求响应参数
interface ResultData<T = any> extends Result {
  data?: T
}
const BaseURL: string = "http://localhost:8000"

enum RequestEnums {
  TIMEOUT = 20000,
  OVERDUE = 600,
  FAIL = 999,
  SUCCESS = 200
}

// 全局设置
const config: AxiosRequestConfig = {
  baseURL: BaseURL,
  timeout: RequestEnums.TIMEOUT,
}


class RequestHttp {
  service: AxiosInstance
  public constructor(config: AxiosRequestConfig) {
    this.service = axios.create(config)

    // 请求拦截器
    this.service.interceptors.request.use(
      (config: InternalAxiosRequestConfig) => {
        return config;
      },
      (error: AxiosError) => {
        // 请求报错
        Promise.reject(error)
      }
    )

    // 响应拦截器
    this.service.interceptors.response.use(
      (response: AxiosResponse) => {
        return response
      },
      (error:AxiosError) => {
        // return error
        const {response} = error
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
        ElMessage.error("Login Error")
        break
      default:
        ElMessage.error("请求失败")
        break
    }
  }

  get<T>(url: string, config?:object): Promise<ResultData<T>> {
    return this.service.get(url, config)
  }

  post<T>(url: string, data?: object, config?:object): Promise<ResultData<T>> {
    return this.service.post(url, data, config)
  }

  stream<T>(url: string, data?:object, config?:object): Promise<ResultData<T>>{
    return this.service.post(url, data, {
      ...config,
      headers: {
        "content": 'application/x-www-form-urlencoded;charset=utf-8',
      },
      responseType: typeof window === undefined ? "stream" : "blob"
    })
  }
}

export default new RequestHttp(config)
