import logging
import json
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def invoke_titan_model(bedrock_client, model_id, input_text, max_token_count, temperature, top_p):
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


    text_gen_config = {
        "maxTokenCount": 150,
        "stopSequences": [], 
        "temperature": 0,
        "topP": 0.9
    }

    body = json.dumps({
        "inputText": input_text,
        "textGenerationConfig": text_gen_config  
    })

    try:
        # Invoke the model
        response = bedrock_client.invoke_model(
            body=body,
            modelId=model_id,
            accept="application/json",
            contentType="application/json"
        )

        # Parse the response body
        response_body = json.loads(response['body'].read())

        # Extract the generated text
        response_text = response_body['results'][0]['outputText']

        logger.info("Response received: %s", response_text)

        return response_text

    except ClientError as err:
        message = err.response['Error']['Message']
        logger.error("A client error occurred: %s", message)
        return f"A client error occurred: {message}"

def main():
    """
    Main function to run the text generation example.
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Model ID and configuration
    model_id = "amazon.titan-text-lite-v1"
    input_text = "who is the actor that plays dan's dad in gossip girl?"
    max_token_count = 512
    temperature = 0.5
    top_p = 0.9

    # Initialize the Bedrock client
    bedrock_client = boto3.client(service_name='bedrock-runtime')

    # Generate the conversation
    response_text = invoke_model(bedrock_client, model_id, input_text, max_token_count, temperature, top_p)

    # Print the response
    print("Generated Text:", response_text)

if __name__ == "__main__":
    main()