from flask import Flask, render_template
import os

app = Flask(__name__)

from routes import *

os.rename("static/videos/video_apresentacao.MP4", "static/videos/video_apresentacao.mp4")
if __name__ == "__main__":
    app.run(debug=True, port=5001)
