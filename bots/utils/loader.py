from langchain.document_loaders import BiliBiliLoader, UnstructuredPDFLoader, PyPDFLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter

# loader = BiliBiliLoader(
#     ['https://www.bilibili.com/video/BV1bp4y137jn/']
# )

class Loader:
    def __init__(self):
        self._loader = None

    async def load_file(self, file_path=None):
        if (file_path is None):
            file_path = "./files/article.txt"
        # self._loader = UnstructuredPDFLoader(file_path)
        self._loader = TextLoader(file_path, "utf-8")
        self._docs = self._loader.load()

    def get_loader(self):
        return self._loader

    async def split(self):
        print("splitting...")
        splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
        self._docs = splitter.split_documents(self._docs)
        print("splitting done")
        return self._docs

# pages = loader.load_and_split()
# print(pages[0])