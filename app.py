from flask import Flask, request, render_template, jsonify
import yt_dlp
import os

app = Flask(__name__)

# Function to download the video
def download_video(video_url, customname):
    download_folder = os.path.join(os.getcwd(), 'downloads')

    # Ensure the downloads folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
     
    ydl_opts = {
'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl': os.path.join(download_folder, f'{customname}%(title)s.%(ext)s'),
    'subtitleslangs': ['en'],
    'noplaylist': True,
    'merge_output_format': 'mp4',
    'ffmpeg_location': 'C:/Users/nandi/Downloads/ffmpeg-7.1-essentials_build/ffmpeg-7.1-essentials_build/bin/',

    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            return True
    except Exception as e:
        return str(e)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the video download
@app.route('/download', methods=['POST'])
def download():
    data = request.json
    video_url = data.get('video_url')
    customname = "Custom_"
    
    if video_url:
        result = download_video(video_url, customname)
        if result == True:
            return jsonify({"message": "Video downloaded successfully!"})
        else:
            return jsonify({"error": result}), 500
    else:
        return jsonify({"error": "No URL provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)
