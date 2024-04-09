from flask import Flask, render_template, jsonify, request
from src.helper import download_embedding
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from src.prompt import *
import os
from flask import Flask, render_template, jsonify, request
from src.helper import download_embedding
from langchain.vectorstores import Pinecone
import pinecone
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from src.helper import text_split
from src.helper import load_pdf


app = Flask(__name__)

load_dotenv()

api_key = os.environ.get("PINECONE_API_KEY")
api_env = os.environ.get("PINECONE_API_ENV")

embeddings = download_embedding()

pinecone.Pinecone(api_key = api_key,
             environment = api_env)

index_name = "medical-chatbot"

docsearch=PineconeVectorStore.from_existing_index(index_name, embeddings)

PROMPT=PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs={"prompt": PROMPT}

llm=CTransformers(model="Model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,
                          'temperature':0.8})

qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True, 
    chain_type_kwargs=chain_type_kwargs)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    result=qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__ == "__main__":
    app.run(debug=True)