from flask import Flask, render_template, request, jsonify
import qrcode
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate_qrcode():
    text = request.args.get('qrcode', '')
    if not text:
        return jsonify({"error": "No text provided for QR code"}), 400

    # Generate QR code
    qr = qrcode.make(text)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    qr_code_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({"qr_code": qr_code_base64})

if __name__ == '__main__':
    app.run(debug=True)
