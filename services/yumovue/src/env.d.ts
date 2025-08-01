declare module '*.vue' {
  import { ComponentOptions } from "vue";
  const componentOptions: ComponentOptions
  export default componentOptions
}

// 声明vue模块，解决computed等API的类型问题
declare module 'vue' {
  export * from '@vue/runtime-dom';
  export { computed, ref } from 'vue';
  export const createSSRApp: typeof import('@vue/runtime-dom').createSSRApp;
}

// 扩展全局属性类型
declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $requests: typeof requests;
  }
}

interface Window {
  __INITIAL_STATE__?: string;
}
