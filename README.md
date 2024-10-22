* YouTube Video Downloader
This project is a YouTube Video Downloader web application that allows users to download videos directly from YouTube by providing the video URL. The frontend is built using HTML, CSS, and JavaScript, while the backend is powered by Flask and yt-dlp for handling the actual video download.

* Table of Contents
->Features
->Technologies Used
->Installation and Setup
->Usage
->Project Structure

* Features
Accepts a YouTube URL as input.
Downloads the video in various formats (such as MP4) using yt-dlp.
Provides a simple, user-friendly web interface.
Shows the status of the download (success message after download).
Efficient and fast video downloads without requiring the user to install additional software.

* Technologies Used
1.Frontend:
HTML5 for structure
CSS3 for styling
JavaScript for interactivity
2.Backend:
Python 3.x: The main programming language used for server-side logic.
Flask: A lightweight web framework for Python used to serve the web pages and handle download requests.
yt-dlp: A command-line tool used for downloading videos from YouTube, integrated into the backend.
3.Other:
Git: For version control.
Virtual Environment: To manage dependencies.

* Installation and Setup
To run the project locally, follow the steps below:

1. Clone the repository:
bash
Copy code
git clone https://github.com/Bhavananandhi/Youtube_videoDownloader.git
cd Youtube_videoDownloader
2. Set up a virtual environment:
bash
Copy code
python -m venv venv
source venv/bin/activate  # For Windows use: .\venv\Scripts\activate
3. Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
4. Run the Flask application:
bash
Copy code
flask run
The app will be running at http://127.0.0.1:5000/. Open this link in your browser.

* Usage
Open the web application in your browser.
Paste a YouTube URL into the input field.
Press the Download button.
After the download completes, a success message will be displayed.
