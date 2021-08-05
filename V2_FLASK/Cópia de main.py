from fastapi import FastAPI
from flask import Flask
from utils.io_utils import load_config
from utils.model_utils import load_model, load_tokenizer, predict_comment

config = load_config()
model = load_model(config['paths']['model'])
tokenizer = load_tokenizer(config['paths']['tokenizer'])

app = Flask(__name__)
#app = FastAPI()

@app.route('/')
def home():
    return render_template('index.html')

@app.get("/prediction")
def predict(comment):
  api_result = predict_comment(comment, tokenizer, model)
  return api_result

##### Colab Run API #####
import nest_asyncio
from pyngrok import ngrok
import uvicorn

ngrok_tunnel = ngrok.connect(8501)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
