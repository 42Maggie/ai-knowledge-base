# AI知识库自动清洗脚本
# 输入：raw_resources.txt
# 输出：clean_resources.md（Markdown表格）
# 修复：跳过文件头、空行；准确统计资源条数

input_file = "raw_resources.txt"
output_file = "clean_resources.md"

# 读取所有行
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 过滤有效行：跳过空行 + 跳过文件头（如 data/raw_resources.txt）
valid_lines = []
for line in lines:
    line = line.strip()
    if not line:  # 跳过空行
        continue
    # 跳过明显是文件路径的行（包含 / 或 .txt）
    if '/' in line or line.endswith('.txt') or not line[0].isdigit():
        continue
    valid_lines.append(line)

# 写入 Markdown 表格
with open(output_file, "w", encoding="utf-8") as f:
    f.write("| 序号 | 标题 | 链接 | 摘要 |\n")
    f.write("|------|------|------|------|\n")
    for i, line in enumerate(valid_lines, 1):
        parts = line.split(" ", 2)
        if len(parts) >= 3:
            num = parts[0].rstrip('.')  # 去掉末尾的点
            url = parts[1]
            summary = parts[2]
            # 提取标题：URL最后一段，替换-为空格，截取前40字符
            title = url.split("/")[-1].replace("-", " ")[:40].strip()
            f.write(f"| {i} | [{title}]({url}) | {url} | {summary} |\n")
        else:
            f.write(f"| {i} | {line} | - | - |\n")

print(f"清洗完成！生成 {output_file}，共 {len(valid_lines)} 条")
