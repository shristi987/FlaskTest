from flask import Flask, jsonify, request

app = Flask(__name__)  # ✅ Gunicorn needs this

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

@app.route("/api/greet")
def greet():
    name = request.args.get("name", "stranger")
    return jsonify({
        "message": f"Hello, {name}!"
    })

@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({
        "you_sent": data
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# Optional: only for local testing, ignored by Gunicorn
if __name__ == "__main__":
    app.run(debug=True)
