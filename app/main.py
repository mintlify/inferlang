from flask import Flask
from guesslang import Guess

guess = Guess()

app= Flask(__name__)
@app.route('/<code>')
def infer(code):
  language = guess.language_name(code)
  return language