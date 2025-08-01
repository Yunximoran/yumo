import { createPinia } from 'pinia'
import { useAnswerStor } from './answer'

const pinia = createPinia()
useAnswerStor(pinia)

export default pinia
