# 智能客服系统2025

## 功能描述
该代码示例实现了一个基础版的智能客服工具，可用于回答用户常见问题。

## 使用方法
1. 安装依赖库：`pip install scikit-learn`
2. 将代码保存为`utils.py`并调用其中的函数。

## 示例
```python
from utils import preprocess_text, extract_keywords

input_text = "请问如何重置密码？"
processed_text = preprocess_text(input_text)
keywords = extract_keywords(processed_text)
print("处理后的文本:", processed_text)
print("提取的关键词:", keywords)
```
输出结果将显示处理后的文本及其提取的关键词。