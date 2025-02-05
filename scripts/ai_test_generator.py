import openai
import os
import re

# Load API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_test_code(test_code: str) -> bool:
    """
    Validate the structure of the generated test code.
    - Checks for the presence of pytest imports.
    - Ensures functions are defined with test function names.
    """
    # Check if pytest is imported
    if 'import pytest' not in test_code:
        print("Error: 'pytest' is not imported in the generated test code.")
        return False

    # Check if there's at least one test function in the generated code
    test_functions = re.findall(r'def test_\w+', test_code)
    if not test_functions:
        print("Error: No test functions found in the generated code.")
        return False
    
    print(f"Found {len(test_functions)} test functions.")
    return True

def generate_tests():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construct the full path to app.py
    app_file_path = os.path.join(repo_root, "app.py")

    # Open the file
    with open(app_file_path, "r") as f:
        code_snippet = f.read()

    prompt = f"Generate unit tests for this Python code using pytest:\n{code_snippet}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": prompt}]
    )

    test_code = response.choices[0].message.content  # Correct way to access the content

    # Validate the generated test code
    if not validate_test_code(test_code):
        print("Generated test code is invalid. Exiting.")
        return

    tests_dir = os.path.join(repo_root, 'tests')
    os.makedirs(tests_dir, exist_ok=True)  # This will create the directory if it doesn't exist

    test_file_path = os.path.join(tests_dir, "test_app.py")
    
    # Write the generated test code to test_app.py
    with open(test_file_path, "w") as f:
        f.write(test_code)
    
    print("AI-Generated Unit Tests:\n", test_code)

if __name__ == "__main__":
    generate_tests()
