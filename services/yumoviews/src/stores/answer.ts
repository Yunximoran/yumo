import { defineStore } from "pinia";


export const useAnswerStor = defineStore("answer", {
  state: () => ({
    answer: "",
    status: false, // 提交状态
    historys: []
  }),

  getters: {
    activate: (state) => {
      return state.historys.length != 0
    }
  },
  actions: {
    ChangeStatus() {
      this.status = !this.status
    },
    // 添加历史提问
    PushQuestion(question:string){
      this.historys.push({
        type: "question",
        content: question
      })
      this.ChangeStatus()
    },

    // 添加历史回答
    PushAnswer(answer: string) {
      this.historys.push({
        type: "answer",
        content: answer
      })
      this.ChangeStatus()
    }
  }
})


