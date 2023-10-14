import os
import logging
from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper
from langchain.llms import OpenAI
import openai
import warnings
os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.environ["OPENAI_API_KEY"]

from llama_index import ServiceContext, StorageContext, load_index_from_storage

warnings.filterwarnings("ignore")


def createIndex(path):
    max_input = 4096
    tokens = 256
    chunk_size = 600
    prompthelper = PromptHelper(max_input, tokens, chunk_overlap_ratio=0.1, chunk_size_limit=chunk_size)
    # define LLM
    llmPredictor = LLMPredictor(llm=OpenAI(temprature=0, model_name="text-ada-001", max_tokens=tokens))
    # Load data
    docs = SimpleDirectoryReader(path).load_data()
    # create vector index
    service_context = ServiceContext.from_defaults(llm_predictor=llmPredictor, prompt_helper=prompthelper)
    vectorIndex = GPTVectorStoreIndex.from_documents(documents=docs, service_context=service_context)
    vectorIndex.storage_context.persist(persist_dir='stored')
    return vectorIndex


def answerMe(question):
    storage_context = StorageContext.from_defaults(persist_dir='stored')
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response
