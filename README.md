# README

## Overview

This script sets up an AI assistant using the Phi framework, which leverages OpenAI's models to interact with a PDF knowledge base. The assistant can continue previous sessions or start new ones, storing the session data in a PostgreSQL database.

## Requirements

- Python 3.8+
- PostgreSQL
- Required Python packages (install via `pip install -r requirements.txt`)

## Setup

1. Clone the repository.
2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
3. Set up your environment variables. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    GROQ_API_KEY=your_openai_api_key
    ```

## Components

- **Agent**: The main AI agent.
- **OpenAIChat**: Interface to OpenAI's chat model.
- **PDFUrlKnowledgeBase**: Loads and processes PDF documents from URLs.
- **Assistant**: Manages the interaction with the user.
- **PgAssistantStorage**: Stores session data in PostgreSQL.
- **PgVector2**: Vector database for embedding storage.

## Notes

- Ensure the PostgreSQL database URL is correctly set in the script.
- The PDF URL in the script should be accessible and valid.
