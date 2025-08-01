<template>
  <div class="home">
    <div class="home sidebar">
      <!-- 侧边栏 -->
      <span v-if="settings" @click="checkmethod_settings">设置</span>
      <span v-else @click="checkmethod_settings">设置选项</span>
    </div>

    <!-- 工作区 -->
    <div class="space area">
      <!-- 回答区域 -->
      <div class="reply" ref="reply" v-if="activate">
        <div v-for="(msg, index) in historys" :key="index" :class="['message', msg.type]">
          <p>{{ msg.content }}</p>
        </div>
        <div v-show="answer !== ''" class="message answer">
          <p>{{ answer }}</p>
        </div>
      </div>

      <!-- 提问区域 -->
      <div class="ask questions">
        <textarea ref="question" v-if="question !== false" v-model="question" @input="update_area_question">
        </textarea>
        <button>
          <img src="../assets/icons/links.png" alt="上传文件" />
        </button>
        <button @click="submit_questions">
          <img src="../assets/icons/run.png" alt="提交问题" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { useAnswerStor } from '@/stores/answer'
import { nextTick } from 'vue'
export default {
  setup() {
    const answerStore = useAnswerStor()
    return {
      answerStore
    }
  },
  data() {
    return {
      // msglist: [],
      question: false,
      settings: true,
      answer: "",
      subing: false
    }
  },
  computed: {
    historys() {
      return this.answerStore.historys
    },
    activate() {
      return this.answerStore.activate
    }
  },
  methods: {
    update_area_question() {
      // 更新提问区高度
      this.$refs.question.style.height = "auto"
      let newHeight = this.$refs.question.scrollHeight
      const maxHeight = 180

      // 限制最大高度
      if (newHeight > maxHeight) {
        newHeight = maxHeight
      }
      this.$refs.question.style.height = newHeight + 'px'
    },

    reset_area_question() {
      this.$refs.question.style.height = 'auto'
      this.question = ''
    },


    submit_questions() {
      if (this.answerStore.status) return

      this.answerStore.PushQuestion(this.question)
      fetch("http://localhost:8000/aigc/answer/", {
        method: "POST",
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
          question: this.question
        })
      }).then(resp => {
        if (!resp.ok) {
          throw new Error("Stream error")
        }
        const reader = resp.body.getReader()
        const decoder = new TextDecoder()

        const readchunk = async () => {
          const { done, value } = await reader.read(); // 异步读取
          if (done) return this.answer;
          // 流结束时退出
          const chunk = decoder.decode(value, { stream: true });
          if ( chunk !== "None") this.answer += chunk;
          return readchunk();
        }

        return readchunk()
      }).then((answer) => {
        // 更新历史记录
        this.answerStore.PushAnswer(answer)
        this.answer = ""

      }).catch(err => {
        this.answerStore.ChangeStatus()
        console.log(err)
      })

      this.reset_area_question()
    },

    checkmethod_settings() {
      this.settings = !this.settings
    },

    scrolltobutton(){
      // 更新滚动条
      nextTick(()=>{
        if (this.$refs.reply) {
          this.$refs.reply.scrollTo({
            top: this.$refs.reply.scrollHeight,
            behavior: 'smooth'
          })
        }
      })
    }
  },
  mounted() {
    this.question = ''
  },
  watch: {
    historys(){
      this.scrolltobutton()
    },
    answer() {
      this.scrolltobutton()
    }
  }
}

</script>

