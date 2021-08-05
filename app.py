from flask import Flask, render_template, request
from fastapi import FastAPI
import json
from utils.io_utils import load_config
from utils.model_utils import load_model, load_tokenizer, predict_comment

##### Colab Run API/FLASK #####
"""import nest_asyncio
from pyngrok import ngrok
import uvicorn"""

app = Flask(__name__)

config = load_config()
model = load_model(config['paths']['model'])
tokenizer = load_tokenizer(config['paths']['tokenizer'])

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
  data = request.form['comment']
  api_result = predict_comment(data, tokenizer, model)
  return render_template('index.html',prediction_text=api_result)

if __name__ == "__main__":
  #ngrok_tunnel = ngrok.connect(5000)
  #print('Public URL:', ngrok_tunnel.public_url)
  #nest_asyncio.apply()
  #uvicorn.run(app, port=8000)
  app.run(debug=True)
  
  








    
  
