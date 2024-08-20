import subprocess
import webbrowser
import time

# Function to start the Flask server
def start_server():
    subprocess.Popen(["python", "app.py"])

# Function to open the web browser
def open_browser():
    time.sleep(2)  # Wait for the server to start
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    start_server()
    open_browser()
