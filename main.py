from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/')
def server_static(path):
    return 


if __name__ == '__main__':
    app.run()
