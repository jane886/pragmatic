# 倒排索引是一种将关键字映射到文档的数据结构。这种数据结构使得查找出现某个单词的文档变得很简单。
# 当用户搜索某个查询时，倒排索引用于检索与查询中的关键字匹配的所有文档。

from collections import defaultdict
import string


def normalize_string(input_string: str) -> str:
    translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    string_without_punc = input_string.translate(translation_table)
    string_without_double_spaces = ' '.join(string_without_punc.split())
    return string_without_double_spaces.lower()


# 为了实现倒排索引，我使用了带有签名 dict[str, dict[str, int]] 的 defaultdict 。
# 这是一个给定单词 (a str ) 的映射，返回从 URL (a str ) 到该单词在 URL 中出现的次数的另一个映射 (a int ）。
# 映射的默认值是从 URL 到 0 的映射，因此如果我们尝试获取 URL 中不存在的关键字的值，我们会得到零。
class SearchEngine:

        # 倒排索引的逻辑是在名为 SearchEngine 的类中定义的。我们用两个私有字典初始化它。
    def __init__(self):
        self._index: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        self._documents: dict[str, str] = {}

        # 然后我们实现 index 方法，它接收 URL 及其内容，规范化内容（即：删除标点符号，所有内容都小写等），然后将其添加到索引中。
    def index(self, url: str, content: str) -> None:
        self._documents[url] = content
        words = normalize_string(content).split(" ")
        for word in words:
            self._index[word][url] += 1

        # 为了使索引过程更可用，我们可以实现批量索引选项，该选项接收 URL 和文档列表并对它们进行索引。
    def bulk_index(self, documents: list[tuple[str, str]]):
        for url, content in documents:
            self.index(url, content)

        # 最后，我们可以使用 get_url 方法读取索引，该方法接收关键字并返回包含该关键字的 URL。
    def get_urls(self, keyword: str) -> dict[str, int]:
        keyword = normalize_string(keyword)
        return self._index[keyword]

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} \n>\n'.format(classname, s)


log = print


def __main():
    pass
    # 例如，要使用文本 Hello, World! My name is Foo! 索引文档 Foo ，使用文本 Hello, World! My name is Bar, I'm not Foo! 索引文档 Bar ，
    # 然后搜索单词 Foo ，我们可以这样做
    engine = SearchEngine()
    log("engine", engine)

    engine.index("Foo", "Hello, World! My name is Foo!")
    engine.index("Bar", "Hello, World! My name is Bar, I'm not Foo!")
    log("engine", engine)

    engine.get_urls("foo")

    engine.get_urls("Foo")


if __name__ == '__main__':
    __main()
