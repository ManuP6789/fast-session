from flask import Flask, jsonify, request
from bedrock_titan import invoke_titan_model
from bedrock_claude import invoke_claude_model
from bedrock_claude import invoke_claude_model_suggestion
from flask_cors import CORS
import boto3

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': 'http://localhost:5173'}})


@app.route('/generate_titan', methods=['POST'])
def generate_titan_text():
    # Get input text from the request
    post_data = request.get_json()
    input_text = post_data.get('input_text')
    
    # Bedrock model configuration
    model_id = "amazon.titan-text-lite-v1"
    max_token_count = 150
    temperature = 0.5
    top_p = 0.9

    # Initialize the Bedrock client
    bedrock_client = boto3.client(service_name='bedrock-runtime')

    # Generate the text
    generated_text = invoke_titan_model(bedrock_client, model_id, input_text, max_token_count, temperature, top_p)

    # Return the generated text as JSON
    return jsonify({'generated_text': generated_text})


@app.route('/generate', methods=['POST'])
def generate_claude_coach():
    # Get input text from the request
    post_data = request.get_json()
    input_text = post_data.get('input_text')
    prev_coach_response = post_data.get('coach_text_history')
    prev_user_question = post_data.get('user_text_history')
    user_goals = post_data.get('user_goals')
    user_major = post_data.get('user_major')
    user_grade = post_data.get('user_grade')
    
    # Bedrock model configuration
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    additional={"top_k":250}

    # Initialize the Bedrock client
    bedrock_client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

    # Generate the text
    generated_text = invoke_claude_model(bedrock_client, model_id, input_text, 
            prev_coach_response, prev_user_question, user_goals, 
            user_major, user_grade, additional)

    # Return the generated text as JSON
    return jsonify({'generated_text': generated_text})

@app.route('/generateSuggestion', methods=['POST'])
def generate_claude_suggestion():
    # Get input text from the request
    post_data = request.get_json()
    prev_coach_response = post_data.get('coach_text_history')
    prev_user_question = post_data.get('user_text_history')
    user_goals = post_data.get('user_goals')
    user_major = post_data.get('user_major')
    user_grade = post_data.get('user_grade')
    
    # Bedrock model configuration
    model_id = "anthropic.claude-3-haiku-20240307-v1:0"
    additional={"top_k":250}

    # Initialize the Bedrock client
    bedrock_client = boto3.client(service_name='bedrock-runtime', region_name="us-east-1")

    print("bedrock_client:", bedrock_client)
    print("model_id:", model_id)
    print("prev_coach_response:", prev_coach_response)
    print("prev_user_question:", prev_user_question)
    print("user_goals:", user_goals)
    print("user_major:", user_major)
    print("user_grade:", user_grade)
    print("additional:", additional)

    # Generate the text
    generated_text = invoke_claude_model_suggestion(bedrock_client, model_id, prev_coach_response, prev_user_question, user_goals, user_major, user_grade, additional)
    print(generated_text)
    # Return the generated text as JSON
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run()
