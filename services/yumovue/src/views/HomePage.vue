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
      <div class="reply" v-if="msglist.length > 0">
        <div v-for="(msg, index) in msglist" :key="index" :class="['message', msg.type]">
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
export default {
  data() {
    return {
      msglist: [],
      question: false,
      settings: true,
      answer: "",
      subing: false
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
      if (this.subing) return
      else this.subing = true
      this.msglist.push({
          type: "question",
          content: this.question
      })

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
        this.msglist.push({
              type: "answer",
              content: answer
        })
        this.answer = ""
        this.subing = false
      }).catch(err => {
        console.log(err)
      })

      this.reset_area_question()
    },
    checkmethod_settings() {
      this.settings = !this.settings
    }
  },
  mounted() {
    this.question = ''
  }
}

</script>

<style>
.home {
  display: flex;
  width: 100%;
  height: 80vh;
  color: aqua;
  flex-direction: row;
}

.home .sidebar {
  left: 10px;
  width: 30px;
  flex-shrink: 0;
}

/* 工作区样式 */
.home .area {
  display: flex;
  flex-grow: 1;
  flex-direction: column;
  justify-content: center;
}

/* 回答区样式 */
.home .reply {
  display: flex;
  flex: 1;
  flex-direction: column;
  overflow: auto;
  padding: 20px;
  gap: 25px;
}

.home .reply .message {
  max-width: 64%;
  padding: 20px;
  border-radius: 18px;
  line-height: 1.6;
  position: relative;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  animation: fadeIn 0.3s ease-out;
  font-size: 17px;
  word-break: break-word;
}

.home .reply .question {
  align-self: flex-end;
}

.home .reply .answer {
  align-self: flex-start;
}

/* 提问区样式 */
.home .area .questions {
  display: flex;
  flex-direction: row;
  height: 64px;
  flex-shrink: 0;
  align-items: flex-end;
  margin: 0 auto;
  gap: 12px;
}

.home .area .questions textarea {
  flex: 1;
  position: relative;
  background: rgba(138, 159, 192, 0.9);
  width: 100%;
  max-height: 200px;
  min-height: 60px;
  max-height: 180px;
  padding: 18px 50px 18px 20px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  color: white;
  font-size: 17px;
  resize: none;
  outline: none;
  line-height: 1.5;
  overflow-y: auto;
  transition: all 0.3s ease;
}

.home .area .questions textarea:focus-within {
  border-color: #4361ee;
  box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.3);
}

.home .area .questions button {
  background-color: transparent;
  border: none;
}

.home .area .questions img {
  /* background-image; */
  width: 20px;
  height: 20px;
  margin: auto;
  display: block;
}
</style>
