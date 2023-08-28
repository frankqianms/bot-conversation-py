import os
from abc import ABC, abstractmethod
from typing import List
from langchain.schema import Document
from langchain.chains import RetrievalQA
from langchain.llms import AzureOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import OpenAIEmbeddings
# from bots.utils.models import llm
from langchain.chat_models import AzureChatOpenAI

# set llm language model
os.environ["OPENAI_API_TYPE"]="azure"
os.environ["OPENAI_API_VERSION"]="2023-03-15-preview"
os.environ["OPENAI_API_BASE"]="https://test-failure-assist.openai.azure.com/"
os.environ["OPENAI_API_KEY"]="659be99dc23949af925cc63361992232"
loader = TextLoader('../../article.txt', encoding='utf8')
embedding = OpenAIEmbeddings(
    deployment='text-embedding',
    model='text-embedding-ada-002',
    openai_api_base=os.environ.get("OPENAI_API_BASE"),
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    openai_api_version=os.environ.get("OPENAI_API_VERSION"),
    openai_api_type=os.environ.get("OPENAI_API_TYPE"),
    chunk_size=10
)
index = VectorstoreIndexCreator(embedding=embedding).from_loaders([loader])
llm = AzureChatOpenAI(
    deployment_name='gpt35', 
    model_name='gpt-35-turbo', 
    openai_api_base=os.environ.get("OPENAI_API_BASE"),
    openai_api_key=os.environ.get("OPENAI_API_KEY"),
    openai_api_version=os.environ.get("OPENAI_API_VERSION"),
    openai_api_type=os.environ.get("OPENAI_API_TYPE"),
    temperature=0.3)
print(index)
print(index.query('为什么说此诚危急存亡之秋?', llm=llm))