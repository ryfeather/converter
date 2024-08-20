from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    url = data['url']
    api_url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/custom/"
    querystring = {"url": url, "quality": "320"}

    headers = {
        "x-rapidapi-key": "7c343ea52dmsh29339fa1765d8dcp17f642jsne50f4793cc7a",
        "x-rapidapi-host": "youtube-mp3-downloader2.p.rapidapi.com"
    }

    response = requests.get(api_url, headers=headers, params=querystring)
    data = response.json()

    print(data)  # Debugging: Print the API response

    if data['status'] == 'finished':
        return jsonify({"status": "success", "downloadUrl": data['dlink']})
    else:
        error_message = data.get('message', 'Unknown error occurred.')
        print(f"Error: {error_message}")  # Debugging: Print the error message
        return jsonify({"status": "error", "message": error_message})

if __name__ == '__main__':
    app.run(debug=True)
