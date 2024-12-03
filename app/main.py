from flask import Flask, Blueprint, request, jsonify
#from app.ollama_model import analyze_text
from ollama_model import analyze_text #to run from cmd

app = Flask(__name__)

# Define the blueprint
bp = Blueprint('main', __name__)

@bp.route("/")
def home():
    return "Welcome to the oLlama API!"

@bp.route('/analyze', methods=['POST'])
def analyze():
    """
    Endpoint to analyze text and extract grammatical components.
    """
    # Parse JSON input
    data = request.get_json()
    app.logger.info(f"Received request data: {data}")
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided. Please include "text" in the JSON payload.'}), 400

    text = data['text']


    if not isinstance(text, str) or not text.strip():
        return jsonify({'error': 'Invalid text. The "text" field must be a non-empty string.'}), 400

    try:
        analysis = analyze_text(text)
        app.logger.info(f"Analysis result: {analysis}")
        return jsonify({"analysis": analysis}), 200
    except Exception as e:
        app.logger.error(f"Error in analyze route: {e}")
        return jsonify({'error': 'An internal error occurred while processing the text.'}), 500

# Register the blueprint
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
