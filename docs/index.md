# AI 知识库（20 条资源）

> **自动化清洗 | 在线搜索 | 持续更新**  
> GitHub: [github.com/42Maggie/ai-knowledge-base]((https://github.com/42Maggie/ai-knowledge-base/)

<input type="text" id="search" placeholder="搜索标题、链接或摘要..." onkeyup="searchTable()" style="width:100%;padding:12px;margin:15px 0;font-size:16px;border:1px solid #ccc;border-radius:8px;box-sizing:border-box;">

<table id="resourceTable" style="width:100%;border-collapse:collapse;font-size:15px;">
  <thead style="background:#f0f2f5;">
    <tr>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">序号</th>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">标题</th>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">链接</th>
      <th style="border:1px solid #ddd;padding:10px;text-align:left;">摘要</th>
    </tr>
  </thead>
  <tbody>

| 1 | [RAG原理全解析](https://blog.csdn.net/mingzai624/article/details/137343216) | https://blog.csdn.net/mingzai624/article/details/137343216 | 图解RAG流程 |
| 2 | [手撸RAG系统](https://www.cnblogs.com/Jcloud/p/18252361) | https://www.cnblogs.com/Jcloud/p/18252361 | 代码示例建知识库 |
| 3 | [阿里云RAG知识库](https://help.aliyun.com/zh/model-studio/rag-knowledge-base) | https://help.aliyun.com/zh/model-studio/rag-knowledge-base | 文本切分指南 |
| 4 | [RAG技术调查](https://blog.csdn.net/leichangqing/article/details/137580712) | https://blog.csdn.net/leichangqing/article/details/137580712 | Naive/Advanced对比 |
| 5 | [Prompt工程指南](https://www.promptingguide.ai/zh) | https://www.promptingguide.ai/zh | 50+技巧 |
| 6 | [Milvus入门](https://milvus.io/docs/zh/quickstart.md) | https://milvus.io/docs/zh/quickstart.md | 向量数据库安装 |
| 7 | [LangChain教程](https://python.langchain.com/docs/get_started/introduction) | https://python.langchain.com/docs/get_started/introduction | RAG框架 |
| 8 | [PaddleNLP RAG](https://paddlenlp.readthedocs.io/zh/latest/examples/rag.html) | https://paddlenlp.readthedocs.io/zh/latest/examples/rag.html | 飞桨代码 |
| 9 | [AI读论文工具](https://zhuanlan.zhihu.com/p/687558511) | https://zhuanlan.zhihu.com/p/687558511 | 10款神器 |
| 10 | [大模型RAG综述](https://zhuanlan.zhihu.com/p/675509396) | https://zhuanlan.zhihu.com/p/675509396 | 一文读懂 |
| 11 | [向量数据库通俗讲解](https://blog.csdn.net/m0_59235699/article/details/141035892) | https://blog.csdn.net/m0_59235699/article/details/141035892 | 图解为什么用 |
| 12 | [飞桨向量教程](https://www.bilibili.com/video/BV1H7RgYCEUf) | https://www.bilibili.com/video/BV1H7RgYCEUf | 免费环境跑代码 |
| 13 | [RAG从0到1教程](https://blog.csdn.net/2401_82469710/article/details/150490601) | https://blog.csdn.net/2401_82469710/article/details/150490601 | 保姆级 |
| 14 | [B站RAG全教程](https://www.bilibili.com/video/BV1H7RgYCEUf) | https://www.bilibili.com/video/BV1H7RgYCEUf | 手把手 |
| 15 | [阿里云百炼知识库](https://help.aliyun.com/zh/model-studio/rag-knowledge-base) | https://help.aliyun.com/zh/model-studio/rag-knowledge-base | 官方指南 |
| 16 | [Prompt最佳实践](https://help.aliyun.com/zh/bailian/best-practices) | https://help.aliyun.com/zh/bailian/best-practices | 阿里云案例 |
| 17 | [Milvus实战](https://milvus.io/docs/zh/quickstart.md) | https://milvus.io/docs/zh/quickstart.md | Docker一键 |
| 18 | [飞桨LLM宇宙](https://github.com/datawhalechina/llm-universe) | https://github.com/datawhalechina/llm-universe | 开源项目 |
| 19 | [向量数据库生活化](https://www.cnblogs.com/pmo-sh/p/about-vector-database.html) | https://www.cnblogs.com/pmo-sh/p/about-vector-database.html | 人脸识别例子 |
| 20 | [AI知识库优化](https://zhuanlan.zhihu.com/p/1893375709315044159) | https://zhuanlan.zhihu.com/p/1893375709315044159 | Indexing/Retrieval |

  </tbody>
</table>

<script>
function searchTable() {
  let input = document.getElementById("search").value.toLowerCase();
  let rows = document.querySelectorAll("#resourceTable tbody tr");
  rows.forEach(row => {
    let text = row.textContent.toLowerCase();
    row.style.display = text.includes(input) ? "" : "none";
  });
}
</script>

<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 20px; line-height: 1.6; }
  table { margin-top: 20px; }
  th, td { border: 1px solid #ddd; padding: 10px; }
  th { background: #f0f2f5; }
  tr:hover { background: #f9f9f9; }
  input::placeholder { color: #999; }
</style>
