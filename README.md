# 小白从 0 到 1 的 AI 知识框架

> **持续更新 | 零基础友好 | 最后更新：2025.10.23**  
> 目标：系统掌握 AI 知识库核心技术（**大模型 → Prompt → 向量 → RAG**）

---

## 模块 1：AI 基础（大模型入门）

| 目标 | 核心资源 | 学习方法 | 实践输出 |
|------|----------|----------------------|---------------------------|
| 理解 LLM 是什么、为什么需要知识库 | 1. [通俗解构语言大模型（知乎）](https://zhuanlan.zhihu.com/p/647476037)<br>2. [大模型 LLM 深入浅出（CSDN）](https://blog.csdn.net/SmallTenMr/article/details/133066350)<br>3. [B站：15分钟搞定 LLM](https://www.bilibili.com/video/BV189W7zCEyU) | 1. 观看视频 **5-10 分钟**，暂停记 **3 个关键词**。<br>2. 读文章 **标题 + 例子**，写 **3 个“是什么”、2 个“为什么”**（<10min）。<br>3. 用通义千问总结：<br>`Prompt: “用故事解释大模型，提取3个核心点”`（<5min）。<br>4. 合并笔记 → `notes/module1_summary.md`。 | 用文心一言写 **AI 知识库介绍** → 保存为 `notes/module1_summary.md`。<br>**联动模块3**：将输出句子用于 `vector_demo.py` 做相似度测试。 |

---

## 模块 2：Prompt 工程（学会“问”AI）

| 目标 | 核心资源 | 学习方法 | 实践输出 |
|------|----------|----------------------|---------------------------|
| 掌握提问技巧，提升输出质量 | 1. [Prompt 工程指南（中文）](https://www.promptingguide.ai/zh)<br>2. [阿里云文生文 Prompt](https://help.aliyun.com/zh/model-studio/prompt-engineering-guide)<br>3. [B站：Prompt 迭代技巧](https://www.bilibili.com/video/BV1h1421t7nE) | 1. 浏览 **1-2 个技巧**（5min）。<br>2. 测试 **3 个变体 Prompt**，记录输出（<10min）。<br>3. 用 AI 优化：<br>`Prompt: “改进这个提问，让它更精确”` → 迭代 **2 次**。<br>4. 总结成 **表格**：输入 / 输出 / 改进点。 | 写 Prompt 总结 RAG 原理 → 保存为 `prompts/rag_summary.txt`。<br>**联动模块4**：将此 Prompt 用于 `rag_demo.py` 的输入优化。 |

---

## 模块 3：向量数据库（知识“怎么存/搜”）

| 目标 | 核心资源 | 学习方法 | 实践输出 |
|------|----------|----------------------|---------------------------|
| 理解向量 = 语义坐标，检索 = 找邻居 | 1. [向量数据库小白读懂（知乎）](https://zhuanlan.zhihu.com/p/667447891)<br>2. [向量数据库图解（CSDN）](https://blog.csdn.net/csdn1561168266/article/details/138609901)<br>3. [向量数据库生活化（博客园）](https://www.cnblogs.com/pmo-sh/p/about-vector-database.html) | 1. 读 **1 篇**（5min），记 **1 个“是什么”、2 个生活例子**。<br>2. 看图解，写 **3 个“怎么作用”**（忽略代码）。<br>3. 用 AI 讲故事：<br>`Prompt: “用超市找商品比喻向量检索”`（<5min）。<br>4. 画 **1 张流程图**（飞书/手绘拍照）。 | 用 Python 模拟相似度 → 保存为 `scripts/vector_demo.py`。<br>**联动模块1**：输入 **模块1 的 5 句笔记**，输出相似度排名。 |

---

## 模块 4：RAG 系统（整合成智能知识库）

| 目标 | 核心资源 | 学习方法 | 实践输出 |
|------|----------|----------------------|---------------------------|
| 构建“检索 + 生成”问答系统 | 1. [RAG 从 0 到 1（CSDN）](https://blog.csdn.net/2401_82469710/article/details/150490601)<br>2. [B站 RAG 全流程](https://www.bilibili.com/video/BV1H7RgYCEUf)<br>3. [阿里云零代码 RAG](https://lilys.ai/notes/zh/agentic-ai-20251020/ai-tutorial-rag-from-scratch-build-ai-chatbot-knowledge-base) | 1. 分步看 **1 个步骤**（10min），记 **1 个检索 + 1 个生成**。<br>2. 用零代码工具测试 **3 个问题**。<br>3. 用 AI 模拟：<br>`Prompt: “步骤分解 RAG 问答”` → 迭代 **1 次**。<br>4. 画 **1 张流程图**（检索 → 生成）。 | 搭建本地 RAG → 保存为 `scripts/rag_demo.py`。<br>**联动模块2**：用 `rag_summary.txt` 的 Prompt 优化输入，测试输出准确率。 |

---

