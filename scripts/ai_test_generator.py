import openai
import os

# Load API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tests():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the full path to app.py
    app_file_path = os.path.join(repo_root, "app.py")

    # Open the file
    with open(app_file_path, "r") as f:
        code_snippet = f.read()

    prompt = f"Generate unit tests for this Python code using pytest:\n{code_snippet}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Use the correct model
        messages=[{"role": "system", "content": prompt}]
    )

    test_code = response['choices'][0]['message']['content']
    tests_dir = os.path.join(repo_root, 'tests')
    os.makedirs(tests_dir, exist_ok=True)  # This will create the directory if it doesn't exist

    with open(os.path.join(tests_dir, "test_app.py"), "w") as f:
        f.write(test_code)
    
    print("AI-Generated Unit Tests:\n", test_code)

if __name__ == "__main__":
    generate_tests()
