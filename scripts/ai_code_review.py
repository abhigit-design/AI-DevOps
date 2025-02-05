import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code():
    with open("app.py", "r") as file:
        code = file.read()

    prompt = f"Review this Python code for best practices and improvements:\n{code}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    print("AI Code Review Report:\n", response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    review_code()
