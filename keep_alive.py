# This bot is kept alive using Replit and UpTimeRobot

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Aternos Bot is Online!"
def run():
  app.run(host='0.0.0.0', port=8080)
def keep_alive():
  t = Thread(target=run)
  t.start()