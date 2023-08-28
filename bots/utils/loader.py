from langchain.document_loaders import BiliBiliLoader, UnstructuredPDFLoader

# loader = BiliBiliLoader(
#     ['https://www.bilibili.com/video/BV1bp4y137jn/']
# )
loader = UnstructuredPDFLoader("")


print(loader.load())