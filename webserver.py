  from flask import Flask
  from threading import Thread

  app = Flask(__name__)

  @app.route('/')
  def home():
      return "Hello, I am alive!"  # Koyeb health checks require this

  def run():  # Renamed from `start_server` to match your main.py
      app.run(host='0.0.0.0', port=8000)  # Must use port 8000 for Koyeb

  def keep_alive():
      Thread(target=run).start()