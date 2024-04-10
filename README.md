# medical-chatbot-llama2-model


## create an enviroment
`conda create -n chatbot python=3.8 -y`

## activate enviroment
`conda activate chatbot`

## Install requirements
`pip install -r requirements`


## create .env for keep secret api key
`PINECONE_API_KEY = "put your pinecone api key here"`
`PINECONE_API_ENV = "put your pinecone api enviroment key here"`

## Download the model
model name:
`llama-2-7b-chat.ggmlv3.q4_0.bin`
model link:
`https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main`