import os
from flask import Flask, render_template, jsonify
from llama_index.llms.azure_inference import AzureAICompletionsModel

# Initialize the Azure Llama Model
llm = AzureAICompletionsModel(
    endpoint=os.environ["AZURE_INFERENCE_ENDPOINT"],
    credential=os.environ["AZURE_INFERENCE_CREDENTIAL"],
)

# Initialize Flask app
app = Flask(__name__)

# Define the API endpoint to get lesson content from the Llama model
@app.route('/lesson/<persona>')
def get_lesson(persona):
    # Set up the persona-specific prompt to interact with the Llama model
    prompts = {
        "Calm and Structured Teacher": """
            You are a helpful assistant. Answer in short and use bullet points.
            Persona: Calm and Structured Teacher
            Teach the basics of computers in a calm, structured, and simple manner, suitable for children with autism.
        """,
        "Visual Learner’s Guide": """
            You are a helpful assistant. Answer in short and use bullet points.
            Persona: Visual Learner’s Guide
            Teach the basics of computers in a way that focuses on visual representation, suitable for children with autism.
        """,
        "Interactive and Engaging Mentor": """
            You are a helpful assistant. Answer in short and use bullet points.
            Persona: Interactive and Engaging Mentor
            Teach the basics of computers through interactive activities and engaging examples, suitable for children with autism.
        """,
        "Supportive and Repetitive Teacher": """
            You are a helpful assistant. Answer in short and use bullet points.
            Persona: Supportive and Repetitive Teacher
            Teach the basics of computers by repeating important information in a supportive manner, suitable for children with autism.
        """
    }
    
    # Get the correct prompt based on the selected persona
    prompt = prompts.get(persona, "Please select a valid persona.")
    
    if prompt == "Please select a valid persona.":
        return jsonify({"error": prompt})

    # Generate lesson using Azure Llama model
    try:
        # Generate a response using the Llama model
        response = llm.complete(prompt=prompt, max_tokens=150)
        
        # Debug: Print the response structure
        print(response)
        
        # Accessing the correct response attribute based on the structure (Assuming it has 'text' field)
        lesson_content = response.text  # or response['text'] depending on the structure

        return jsonify({"lesson": lesson_content})
    
    except Exception as e:
        return jsonify({"error": "Failed to generate lesson: {}".format(str(e))})

# Route to serve the index.html page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
