# AI知识库自动清洗脚本
# 输入：raw_resources.txt
# 输出：clean_resources.md（Markdown表格）

input_file = "raw_resources.txt"
output_file = "clean_resources.md"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w", encoding="utf-8") as f:
    f.write("| 序号 | 标题 | 链接 | 摘要 |\n")
    f.write("|------|------|------|------|\n")
    for i, line in enumerate(lines, 1):
        parts = line.strip().split(" ", 2)
        if len(parts) >= 3:
            num, url, summary = parts[0][:-1], parts[1], parts[2]
            title = url.split("/")[-1].replace("-", " ")[:40]
            f.write(f"| {i} | [{title}]({url}) | {url} | {summary} |\n")
        else:
            f.write(f"| {i} | {line.strip()} | - | - |\n")

print(f"清洗完成！生成 {output_file}，共 {len(lines)} 条")
