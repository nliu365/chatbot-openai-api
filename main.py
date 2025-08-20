import openai

# Create an openai client
client = OpenAI()

# Design a simple user message to test the API
prompt = "Hi, can you tell me a joke?"

# Create a chat completion request to get the AI response
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}]
)

# Extract the AI's response from the API result
reply = response.choices[0].message.content.strip()

# Show the conversation thread
print("Prompt:", prompt)
print("Response:", reply)
