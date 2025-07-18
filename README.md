# Skills Trade Chatbox AI Backend

## Description

This is an AI backend using FastAPI, integrated with Ollama (OpenAI API compatible) to process questions from the frontend and return automated answers.

## Requirements

-   Python 3.8+
-   pip
-   [Ollama](https://ollama.com/) (installed and model pulled, e.g. `ollama pull deepseek-r1:8b`)

## Setup

1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd skills-trade-chatbox-ai
    ```
2. Create a virtual environment (recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # (Linux/macOS)
    .venv\Scripts\activate   # (Windows)
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    # Or if requirements.txt is missing:
    pip install fastapi uvicorn openai requests
    ```
4. Start the Ollama server:
    ```bash
    ollama serve
    # Make sure Ollama is running at http://localhost:11434
    ```
5. Run the FastAPI backend:
    ```bash
    uvicorn main:app --reload
    # The server will run at http://localhost:8000
    ```

## API Usage

### Endpoint

-   `POST /ask`
-   Body (JSON):
    ```json
    {
    	"question": "Suggest posts about Design"
    }
    ```
-   Response:
    ```json
    {
    	"answer": "..." // The answer from the AI
    }
    ```

### Example API call with curl

```bash
curl -X POST http://localhost:8000/ask \
     -H "Content-Type: application/json" \
     -d '{"question": "Suggest posts about Design"}'
```

## Notes

-   If you get a 500 error or "Connection refused", make sure Ollama is running on port 11434.
-   You can extend the logic in the `/ask` handler to integrate with other backend APIs, query databases, etc.

## Contact

For support, contact the project admin or open an issue on the repository.
