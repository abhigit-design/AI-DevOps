import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tests():
    with open("app.py", "r") as file:
        code = file.read()

    prompt = f"Generate unit tests for this Python code using pytest:\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    test_code = response["choices"][0]["message"]["content"]
    
    with open("tests/test_app.py", "w") as test_file:
        test_file.write(test_code)

    print("AI-Generated Unit Tests:\n", test_code)

if __name__ == "__main__":
    generate_tests()
