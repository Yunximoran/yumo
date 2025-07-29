const url = 'https://api.siliconflow.cn/v1/chat/completions';
const options = {
  method: 'POST',
  headers: {Authorization: 'Bearer <token>', 'Content-Type': 'application/json'},
  body: '{"model":"Qwen/QwQ-32B","messages":[{"role":"user","content":"What opportunities and challenges will the Chinese large model industry face in 2025?"}]}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
//

const answer = {
    "id": "<string>",
    "choices": [
      {
        "message": {
          "role": "assistant",
          "content": "<string>",
          "reasoning_content": "<string>",
          "tool_calls": [
            {
              "id": "<string>",
              "type": "function",
              "function": {
                "name": "<string>",
                "arguments": "<string>"
              }
            }
          ]
        },
        "finish_reason": "stop"
      }
    ],
    "usage": {
      "prompt_tokens": 123,
      "completion_tokens": 123,
      "total_tokens": 123
    },
    "created": 123,
    "model": "<string>",
    "object": "chat.completion"
  }