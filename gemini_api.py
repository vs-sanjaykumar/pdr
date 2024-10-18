import requests

def get_extracted_details(text, prompt):
    """
    Sends the extracted text and user prompt to the Gemini API to get the extracted details.

    :param text: The extracted text from the OCR process.
    :param prompt: The prompt entered by the user to extract specific details.
    :return: The extracted details or an error message.
    """
    # Use the actual Gemini API URL instead of the placeholder
    api_url = "https://api.gemini.com/extract"  # Replace with the correct Gemini API URL

    # Add API key in the params
    params = {
        'key': 'AIzaSyBwPmE8nCWi9sw_WopPA6RYHVLoWmnj_Lk'  # Replace with your actual API key
    }

    payload = {
        "text": text,
        "prompt": prompt
    }

    try:
        # Make the POST request with API key as a query parameter
        response = requests.post(api_url, params=params, json=payload)

        # Check if the response was successful
        if response.status_code == 200:
            return response.json().get('extracted_details', 'No details extracted')
        else:
            return f"API call failed with status code: {response.status_code}"

    except Exception as e:
        return f"Error during API call: {str(e)}"
