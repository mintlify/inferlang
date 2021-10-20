from flask import Flask, request
from guesslang import Guess

guess = Guess()

app= Flask(__name__)
@app.route('/')
def index():
  return "Welcome to Infercode by Figstack"

@app.route('/infer', methods=['GET', 'POST'])
def infer():
  body = request.json
  code = body['code']
  if (code is not None):
    language = guess.language_name(code)
    return {"success": True, "language": language}

  return { "success": False, "error": "Language not provided" }