from flask import Flask
import sys
sys.path.append('c:\\users\\sim\\anaconda3\\lib\\site-packages')

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, True)