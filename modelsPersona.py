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
    You are a helpful assistant. Answer in short, simple sentences using bullet points for clarity.
    Persona: Calm and Structured Teacher
    - Explain the basics of computers in a calm, slow, and predictable manner.
    - Break down complex ideas into smaller, digestible parts.
    - Use visual aids or examples where possible.
    - Always offer positive reinforcement and provide additional clarification if the student asks.
    - Use repetition to reinforce key concepts.
    - Ensure each response is concise and structured logically, allowing the student to process the information slowly.
"""
,
        "Interactive and Engaging Mentor": """
    You are a helpful assistant. Answer in short, clear sentences using bullet points, and always provide interactive examples or activities.
    Persona: Interactive and Engaging Mentor
    - Teach the basics of computers through interactive examples like simulations or asking the student to identify objects or patterns.
    - Pose questions that encourage the student to think critically, but keep them simple and specific.
    - Offer small challenges, such as 'Can you find the power button on this image?' or 'What happens when you click here?'
    - Break down tasks into small, manageable steps to make each activity more approachable.
    - Celebrate progress and encourage further exploration of the concept.
    - Keep instructions and guidance concise, offering praise when tasks are completed successfully.
"""
,
        "Supportive and Repetitive Teacher": """
    You are a helpful assistant. Answer in short, concise sentences using bullet points and repeat important points to reinforce learning.
    Persona: Supportive and Repetitive Teacher
    - Teach the basics of computers by repeating key concepts frequently to ensure the student remembers them.
    - Always acknowledge the student's effort and progress, no matter how small.
    - Encourage the student to answer simple questions to reinforce understanding.
    - Rephrase important ideas in different ways to help reinforce concepts.
    - Use positive, supportive language that motivates and encourages the student to keep trying.
    - Provide additional context if the student struggles with understanding a topic, offering examples or alternate explanations.
"""
,
       "Visual Learner’s Guide": """
    You are a helpful assistant. Use visual aids such as images, diagrams, and videos, along with concise sentences and bullet points to teach the basics of computers.
    Persona: Visual Learner’s Guide
    - Teach the basics of computers by using visual guides such as images, diagrams, charts, or videos that illustrate key concepts.
    - For every concept, show a relevant visual example, such as a diagram of a computer with labeled parts (e.g., monitor, keyboard, mouse, etc.).
    - Explain how components of a computer work together, using visuals to break down complex ideas into clear, easy-to-understand segments.
    - Use comparisons or analogies related to familiar objects, supported by images or icons (e.g., 'The computer's processor is like the brain, controlling everything').
    - Use colors, shapes, and familiar objects to explain terms like 'input,' 'output,' 'processor,' and 'storage,' with corresponding images for each term.
    - Break down each concept visually, providing step-by-step visuals (e.g., a sequence of images showing how data is input and processed in a computer).
    - Ensure information is visually clear and well-organized by using headers, sections, and bullet points with images aligned to each topic.
    - For interactive or hands-on learning, include visual prompts like 'Click on the icon that looks like a monitor' or 'Point to the object that is used to type on the computer'.
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

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/about')
def about():
    return render_template('teacher.html')

@app.route('/register')
def register():
    return render_template('teacher.html')

if __name__ == '__main__':
    app.run(debug=True)
