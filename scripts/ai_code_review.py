import openai
import os

# Load API Key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code():
    """Uses AI to review the quality and security of the code"""
    with open("../app.py", "r") as f:
        code_snippet = f.read()

    prompt = f"""
    Review the following Python code for security vulnerabilities, performance optimizations, and best practices:
    ```
    {code_snippet}
    ```
    Provide suggestions in bullet points.
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a Python code reviewer."},
                  {"role": "user", "content": prompt}]
    )

    review_feedback = response.choices[0].message.content

    with open("../reports/code_review.txt", "w") as f:
        f.write(review_feedback)

    print("✅ AI Code Review Completed! Report saved to reports/code_review.txt")

if __name__ == "__main__":
    review_code()
