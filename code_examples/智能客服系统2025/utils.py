```python
# utils.py

def preprocess_text(text):
    """
    对输入文本进行预处理，例如去除特殊字符、分词等。
    :param text: str, 输入文本
    :return: str, 处理后的文本
    """
    import re
    cleaned_text = re.sub(r'[\W_]+', ' ', text)
    return cleaned_text.strip()


def extract_keywords(text):
    """
    使用TF-IDF提取文本关键词。
    :param text: str, 输入文本
    :return: list, 关键词列表
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    return feature_names.tolist()
```