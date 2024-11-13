from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configuration settings
app.config['DEBUG'] = True  # Enable debug mode for development
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8080

# Define the main route
@app.route("/")
def hello():
    return "Hello World!"

# Optional additional API route for testing
@app.route("/api/message")
def api_message():
    return jsonify(message="Hello from the API!")

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Page not found"), 404

# Run the application
if __name__ == "__main__":
    app.run(host=app.config['HOST'], port=app.config['PORT'])
