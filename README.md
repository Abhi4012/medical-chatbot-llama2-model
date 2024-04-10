# medical-chatbot-llama2-model

## Clone repo
`link:` https://github.com/Abhi4012/medical-chatbot-llama2-model.git

```git clone https://github.com/Abhi4012/medical-chatbot-llama2-model.git``` clone this repository using `git bash` or `command prompt` in you local system.


## some steps for using this project and run in locaL systems
## create an enviroment
`conda create -n chatbot python=3.8 -y`

## activate enviroment
`conda activate chatbot`

## Install requirements
`pip install -r requirements.txt`


## create .env for keep your secret api key
```pinecone link for creating api key and environment:``` https://www.pinecone.io/
`PINECONE_API_KEY = "put your pinecone api key here"`
`PINECONE_API_ENV = "put your pinecone api enviroment key here"`

## Download the model
model name:
`llama-2-7b-chat.ggmlv3.q4_0.bin`
model link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main


## Run 
`python app.py`