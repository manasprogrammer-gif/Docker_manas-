from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Application deployed successfully through CI/CD pipeline!"

@app.route('/health')
def health():
    return jsonify({"status": "HEALTHY"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
