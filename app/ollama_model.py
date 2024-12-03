import requests
import json

def analyze_text(text):
    """
    Analyze the text using the Ollama API to extract subject, verb, and object.
    """
    # Prompt with the sentence to be analyzed
    prompt = (
        f"Analyze the following sentence and identify its grammatical components:\n\n"
        f"Sentence: {text}\n\n"
        f"Response format: {{'subject': <subject>, 'verb': <verb>, 'object': <object>}}"
    )
    
    # Request body
    request_body = {
        "model": "llama3.2",  
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ]
    }
    
    # URL for the Ollama API endpoint
    url = "http://localhost:11434/api/chat"  
   
    # POST request to the Ollama API
    response = requests.post(url, json=request_body)
    print('STATUS CODE:', response.status_code)
    #print('TEXT:', response.text)

    # Check for successful response
    if response.status_code == 200:
        lines = response.text.strip().split('\n')
        result = ''
        
        # Concatenate each "content" field into a single string
        for line in lines:
            try:
                json_data = json.loads(line)
                result += json_data['message']['content']
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue

        # Check if 'done' is true in the last response part and return the concatenated result
        return {"analysis": result.strip()}  # Return as a JSON object with the concatenated result

    else:
        raise ValueError(f"An error occurred while analyzing the text: {response.json().get('error', 'Unknown error')}")
