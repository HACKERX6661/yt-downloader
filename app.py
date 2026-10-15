from flask import Flask, request, Response
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    # Wir streamen die Datei direkt
    def generate():
        ydl_opts = {'format': 'best', 'noplaylist': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            url_direct = info['url'] # Direkter Link zum Video-Stream
            # Hier müsste man eigentlich einen Proxy-Stream bauen
            # Für den Anfang: Redirect zur Video-URL (intern)
            return url_direct 

    return "Hier kommt der Stream-Code hin", 200
