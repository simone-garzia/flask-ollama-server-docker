# oLlama Flask Project

## Description
A Flask server to analyze sentences using the oLlama model. The server extracts the subject, verb, and object from a sentence.

## Setup Instructions

1. Clone the repository.
### **2. Build the Docker image:**
docker build -f ./Dockerfile -t ollama-flask-app .

### **3. Run the container:**
docker run -p 5000:5000 ollama-flask-app

### **4. Send a POST request to analyze a sentence:**
curl -X POST -H "Content-Type: application/json"
-d '{"text": "The cat sat on the mat."}'
http://localhost:5000/analyze


