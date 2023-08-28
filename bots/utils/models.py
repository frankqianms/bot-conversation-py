import os
# from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI

# set llm language model
os.environ["OPENAI_API_TYPE"]=os.environ.get("OPENAI_API_TYPE")
os.environ["OPENAI_API_VERSION"]=os.environ.get("OPENAI_CHAT_API_VERSION")
os.environ["OPENAI_API_BASE"]=os.environ.get("OPENAI_API_BASE")
os.environ["OPENAI_API_KEY"]=os.environ.get("OPENAI_API_KEY")
llm = AzureChatOpenAI(deployment_name='gpt35', model_name='gpt-35-turbo', temperature=0.3)
# llm = AzureOpenAI(deployment_name='gpt35', model_name='gpt-35-turbo', temperature=0.3)