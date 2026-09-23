from flask import Flask, jsonify, request
import random

app = Flask(__name__)
app.json.sort_keys = False

REGISTRATION_NUMBER = "FA24-BSE-113"

random.seed(REGISTRATION_NUMBER)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

@app.route('/predict', methods=['GET'])
def predict():
    try:
        x1 = float(request.args.get('x1', 0))
        x2 = float(request.args.get('x2', 0))
        x3 = float(request.args.get('x3', 0))
        
        prediction = (a1 * x1) + (a2 * x2) + (a3 * x3) + b
        
        return jsonify({
            "registration number": REGISTRATION_NUMBER,
            "prediction": round(prediction, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
