from flask import Flask
import os

app = Flask(__name__)

from routes import *

try:
    os.rename("static/videos/video_apresentacao.MP4", "static/videos/video_apresentacao.mp4")
except FileNotFoundError:
    pass  

if __name__ == "__main__":
    app.run(debug=True, port=5001)