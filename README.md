# Chatbot with OpenAI

OpenAI’s API provides advanced language models that can read and generate natural text. This makes it an excellent choice for creating chatbots and other conversational tools.

In this project, we start with the basics: sending a single message to OpenAI and receiving a reply. This step is the foundation for building more complex chatbot interactions.

---

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python installed. Then, install the OpenAI Python library:

```bash
pip install openai
```

### 2. Get an API Key
1. Sign up at OpenAI.
2. Add a payment method.
3. Generate an API key from your account dashboard.
4. Keep this key secure and do not hard-code it in your scripts.

### 3. Confiure the API Key
Store your API key as an environment variable so your applications can use it securely.
macOS & Linux (Terminal):
```bash
export OPENAI_API_KEY="your_api_key_here"
```
Windows (Command Prompt):
```bash
set OPENAI_API_KEY=your_api_key_here
```
### 4. Next Step
With the library installed and your API key configured, you’re ready to send your first request and begin building your chatbot.

---
