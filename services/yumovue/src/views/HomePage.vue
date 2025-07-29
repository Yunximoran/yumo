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
          {{ msg.content }}
        </div>
      </div>

      <!-- 提问区域 -->
    	<div class="ask questions">
        	<textarea
            ref="question textarea"
            v-model="message"
            @input="update_area_question"
          >
          </textarea>
        	<button>
        		<img src="../assets/icons/links.png" alt="上传文件" />
        	</button>
        	<button @click="submit">
        		<img src="../assets/icons/run.png" alt="提交问题" />
        	</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useTemplateRef } from 'vue'


/* ============= DATA ============= */
const settings = ref(true)
const msglist = ref([])


/* ============= MODEL ============= */
const message = defineModel()


/* ============= TEMPLATE ============= */
const area_question = useTemplateRef("question textarea") // 提问区


/* ============= METHODS ============= */
// 更新提问区
function update_area_question() {
  // 更新提问区高度
  area_question.value.style.height = "auto"
  let newHeight = area_question.value.scrollHeight
  const maxHeight = 180

  // 限制最大高度
  if (newHeight > maxHeight) {
    newHeight = maxHeight
  }
  area_question.value.style.height = newHeight + "px"
}

// 重置提问区
function reset_area_question(){ // 重置提问区
  area_question.value.style.height = "auto"
  message.value = ""
}

// 提交问题
function submit(event) {
  const question = {
    type : "question",
    content : message.value
  }

  const answer = {
    type: "answer",
    content: "服务器繁忙"
  }

  axios.post(
    'https://api.siliconflow.cn/v1/chat/completions', {
        model: "Qwen/QwQ-32B",
        messages: [{
          role: "user",
          content: question.content,
        }],
        stream: true,
        max_tokens: 512,
    }, {
      headers:{
        // sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr
        Authorization: "Bearer sk-evotgvphlyvrorfrlcwrlounwqkytauesvcfpbrbadivqicr",
        'Content-Type': "application/json"
      },
      responseType: 'stream'
    }
  ).then(res => {
    res.data.on('data', (chunk) =>{

    })
    // console.log(res.data)

  }).catch(err => {
    console.log(err)
  })
  message.value = ''

  // 提交问题信息列表
  msglist.value.push(question)
  msglist.value.push(answer)

  // 重置提问区状态
  reset_area_question()
}

// 打开设置
function checkmethod_settings(event) {
  alert('check settings value')
  settings.value = !settings.value
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
  animation:  fadeIn 0.3s ease-out;
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
