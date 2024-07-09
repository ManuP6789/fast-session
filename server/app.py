from flask import Flask, jsonify, request
from bedrock import invoke_model
from flask_cors import CORS
import boto3

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': 'http://localhost:5173'}})


@app.route('/generate', methods=['POST'])
def generate_text():
    # Get input text from the request
    post_data = request.get_json()
    input_text = post_data.get('input_text')
    
    # Bedrock model configuration
    model_id = "amazon.titan-text-lite-v1"
    max_token_count = 512
    temperature = 0.5
    top_p = 0.9

    # Initialize the Bedrock client
    bedrock_client = boto3.client(service_name='bedrock-runtime')

    # Generate the text
    generated_text = invoke_model(bedrock_client, model_id, input_text, max_token_count, temperature, top_p)

    # Return the generated text as JSON
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run()
