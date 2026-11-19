
from flask import Flask, jsonify, request

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


@app.route("/about")
def about():
    return jsonify({
        "project": "Automated CI/CD DevOps Pipeline",
        "version": "1.0.0",
        "developer": "Rahul",
        "status": "running"
    }), 200


# E-commerce Order Preview API
@app.route("/api/orders/preview", methods=["POST"])
def order_preview():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Valid JSON is required"}), 400

    product = data.get("product")
    quantity = data.get("quantity")
    unit_price_paise = data.get("unit_price_paise")

    if not isinstance(product, str) or not product.strip():
        return jsonify({"error": "Product name is required"}), 400

    if type(quantity) is not int or quantity <= 0:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    if type(unit_price_paise) is not int or unit_price_paise <= 0:
        return jsonify({"error": "Price must be a positive integer in paise"}), 400

    total_paise = quantity * unit_price_paise

    return jsonify({
        "status": "success",
        "order_summary": {
            "product": product.strip(),
            "quantity": quantity,
            "unit_price_paise": unit_price_paise,
            "total_paise": total_paise,
            "currency": "INR"
        }
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
