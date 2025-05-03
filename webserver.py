# web server to keep replit awake 
from flask import Flask
from threading import Thread

#defines as a flask app
app = Flask(__name__)

# defines the home page, and prints "Hello, I am alive!"
@app.route('/')
def home():
  return "Hello, I am alive!"

# defines the host and port
def start_server():
  app.run(host='0.0.0.0', port=8000)

# keeps replit awake
def keep_alive():
  Thread(target=run).start()