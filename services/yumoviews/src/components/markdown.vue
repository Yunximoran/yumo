<template>
  <!-- 使用v-html渲染解析后的HTML -->
  <div class="markdown-content" v-html="renderedMarkdown"></div>
</template>

<script>
import { marked } from 'marked';
import hljs from 'highlight.js';
import 'highlight.js/styles/github-dark.css'; // 导入代码高亮样式

// 配置marked，启用代码高亮
marked.setOptions({
  highlight: function(code, lang) {
    // 如果指定了语言且hljs支持，则高亮代码
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
    // 未指定语言时尝试自动检测
    return hljs.highlightAuto(code).value;
  },
  breaks: true, // 支持换行符转换为<br>
  gfm: true // 支持GitHub Flavored Markdown
});

export default {
  name: 'MarkdownRenderer',
  props: {
    // 接收外部传入的Markdown文本
    source: {
      type: String,
      required: true,
      default: ''
    }
  },
  computed: {
    // 计算属性：将Markdown转换为HTML
    renderedMarkdown() {
      if (!this.source) return '';
      return marked(this.source);
    }
  }
};
</script>


