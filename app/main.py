from flask import Flask
from guesslang import Guess

guess = Guess()

app= Flask(__name__)
@app.route('/')
def index():
  return "Welcome to Infercode by Figstack"

@app.route('/<code>')
def infer(code):
  language = guess.language_name(code)
  return language