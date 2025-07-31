import { createPinia } from 'pinia'
import { useCounterStore } from './counter'

const pinia = createPinia()
useCounterStore(pinia)

export default pinia
// export default () => {
//   const pinia = createPinia()

//   useCounterStore(pinia)
//   return pinia
// }
