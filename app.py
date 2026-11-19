from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD DevOps Project</title>
        </head>
        <body>
            <h1>Welcome to CI/CD DevOps Pipeline!</h1>
            <p>Flask Application is Running Successfully.</p>
            <p>Automated Testing with Pytest and GitHub Actions.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Application is healthy"
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)