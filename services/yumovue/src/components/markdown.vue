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

<style scoped>
/* 基础Markdown样式（可根据需求调整） */
.markdown-content {
  padding: 1rem;
  line-height: 1.8;
}

/* 标题样式 */
.markdown-content h1,
.markdown-content h2,
.markdown-content h3 {
  margin: 1.5rem 0 1rem;
  font-weight: 600;
}

/* 段落样式 */
.markdown-content p {
  margin-bottom: 1rem;
}

/* 列表样式 */
.markdown-content ul,
.markdown-content ol {
  margin: 1rem 0;
  padding-left: 2rem;
}

/* 代码块样式 */
.markdown-content pre {
  padding: 1rem;
  border-radius: 6px;
  margin: 1rem 0;
  overflow-x: auto;
}

.markdown-content code {
  font-family: 'Fira Code', monospace;
  font-size: 0.9rem;
}

/* 链接样式 */
.markdown-content a {
  color: #42b983;
  text-decoration: none;
}

.markdown-content a:hover {
  text-decoration: underline;
}

/* 引用样式 */
.markdown-content blockquote {
  border-left: 4px solid #ddd;
  padding-left: 1rem;
  color: #666;
  margin: 1rem 0;
}
</style>
