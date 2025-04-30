from flask import Flask, jsonify, request

app = Flask(__name__)

# HTML response route
@app.route("/")
def home():
    return """
    <html>
        <head><title>Simple Flask App</title></head>
        <body>
            <h1>Welcome to the Simple Flask App!</h1>
            <p>Go to <a href="/api/greet?name=World">/api/greet?name=World</a> for a JSON response.</p>
        </body>
    </html>
    """

# JSON response route
@app.route("/api/greet")
def greet():
    name = request.args.get("name", "stranger")
    return jsonify({
        "message": f"Hello, {name}!"
    })

# Route that echoes posted JSON data
@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({
        "you_sent": data
    })

# A simple health check route
@app.route("/health")
def health():
    return jsonify({"status": "ok"})


app.run(host="127.0.0.1", port=5000, debug=True)
