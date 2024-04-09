
from src.helper import load_pdf, text_split, download_embedding
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get("PINECONE_API_KEY")
api_env = os.environ.get("PINECONE_API_ENV")


load_data = load_pdf("data/")
text_chunks = text_split(load_data)
embeddings = download_embedding()


#Initializing the Pinecone
# from pinecone import Pinecone as PineconeClient
# pc = PineconeClient(api_key=api_key, environment=api_env)


# index_name="medical-chatbot"

# #Creating Embeddings for Each of The Text Chunks & storing
# docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)


# index_name="medical-chatbot"
# docsearch=Pinecone.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)



# # Initializing the Pinecone
import pinecone
from langchain_pinecone import PineconeVectorStore

import os

#os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
pinecone.Pinecone(api_key = api_key,
             environment = api_env)

index_name = "medical-chatbot"

docsearch = PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name = "medical-chatbot")