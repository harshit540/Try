from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "message": "Calculator API running 🚀"
    }

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        op = data['op']

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return jsonify({"error": "Division by zero"})
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operation"})

        return jsonify({"result": result})

    except:
        return jsonify({"error": "Invalid input"})
