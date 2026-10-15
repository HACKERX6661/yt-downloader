from flask import Flask, request, send_file, render_template_string
import yt_dlp
import os

app = Flask(__name__)

# The HTML is already in your index.html, but this handles the request
@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    filename = "video.mp4"
    
    # We add 'user_agent' to fool YouTube into thinking we are a browser
    ydl_opts = {
        'format': 'best',
        'outtmpl': filename,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e), 500
