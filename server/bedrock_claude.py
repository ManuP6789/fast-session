import logging
import json
import boto3
from botocore.exceptions import ClientError

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def invoke_claude_model(bedrock_client, model_id, input_text, prev_coach_response, prev_user_question, user_goals, user_major, user_grade, additional):
    """
    Sends input text to a model for text generation.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input_text (str): The input text to send to the model.
        max_token_count (int): The maximum number of tokens for the generated text.
        temperature (float): The temperature parameter for text generation.
        top_p (float): The top_p parameter for text generation.

    Returns:
        response (JSON): The response from the model.
    """
    logger.info("Generating text with model %s", model_id)

    user_message = f"""
        You will be acting as an AI career coach named Coach. Your goal is to give career advice to users. You will be replying to users who are on the site and who will be confused if you don't respond in the character of Coach.

        Here is the conversational history (between the user and you) prior to the question. It could be empty if there is no history:
        <history>
        User: {prev_user_question}
        Joe: {prev_coach_response}
        </history>

        Here are some important rules for the interaction:
        - These are the user goals for this conversation: {user_goals}
        - The user is interested in this field: {user_major}
        - This is the grade of the user: {user_grade}
        - If you are unsure how to respond, say "Sorry, I didn't understand that. Could you rephrase your question?"
        - Do not return anything about assuming a role, for example: *takes on the role of Coach*
        - Do not say anything about the tone you use or use *clears throat.. *
        - Respond in 4 paragraphs at most!!! 
        
        Here is the query: {input_text}
    """
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]
    client = bedrock_client


    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens":200,"temperature":1},
            additionalModelRequestFields=additional
        )

        # Parse the response body
        response_text = response["output"]["message"]["content"][0]["text"]
        
        try:
            response_json = json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            response_json = {"text": response_text}  # Return the raw text if JSON parsing fails

        return response_json

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        return f"A client error occurred: {message}"



def invoke_claude_model_suggestion(bedrock_client, model_id, prev_coach_response, prev_user_question, user_goals, user_major, user_grade, additional):
    """
    Sends input text to a model for text generation.
    Args:
        bedrock_client: The Boto3 Bedrock runtime client.
        model_id (str): The model ID to use.
        input_text (str): The input text to send to the model.
        max_token_count (int): The maximum number of tokens for the generated text.
        temperature (float): The temperature parameter for text generation.
        top_p (float): The top_p parameter for text generation.

    Returns:
        response (JSON): The response from the model.
    """
    logger.info("Generating text with model %s", model_id)

    user_message = f"""
        You will be acting as a prompt engineer for a user using an AI career coach named Coach. Your goal is to give suggestions to get better prompts for their career advice to users. You will be giving short 2-3 sentence suggestions to users who are on the site and who will be confused if you don't respond in the character of advisor.

        Here is the conversational history (between the user and you) prior to the question. It could be empty if there is no history:
        <history>
        User: {prev_user_question}
        Joe: {prev_coach_response}
        </history>

        Here are some important rules for the interaction:
        - These are the user's goals for its interaction with career coach conversation: {user_goals}
        - The user is interested in this field: {user_major}
        - This is the grade level of the user: {user_grade}
        - If you are unsure how to respond, do not say anything.
        - Do not return anything about assuming a role, for example: *takes on the role of prompt engineer*

        RETURN ONE SUGGESTION ONLY
    """
    conversation = [
        {
            "role": "user",
            "content": [{"text": user_message}],
        }
    ]
    client = bedrock_client


    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={"maxTokens":50,"temperature":1},
            additionalModelRequestFields=additional
        )

        # Parse the response body
        response_text = response["output"]["message"]["content"][0]["text"]
        
        try:
            response_json = json.loads(response_text)
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            response_json = {"text": response_text}  # Return the raw text if JSON parsing fails
        print(response_json)
        return response_json

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        return f"A client error occurred: {message}"