# AI Agent System

A multi-agent system that provides web search, financial information, and combined agent capabilities using the Phi Framework.

## Features

- **Web Search Agent**: Search and retrieve information from the web
- **Finance Agent**: Get financial data, stock prices, and company information
- **Agent Team**: Combines both agents for comprehensive responses

## Prerequisites

- Python 3.8+
- Required environment variables in `.env` file
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ahzem/new_ai_agent.git
cd new_ai_agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the application:
```bash
python app.py
```

Follow the interactive prompts:
1. Select an agent (1-4)
2. Enter your question
3. View the response

## Project Structure

```
new_ai_agent/
├── agents/
│   ├── __init__.py
│   ├── web_search_agent.py
│   ├── finance_agent.py
│   └── agent_team.py
├── app.py
├── requirements.txt
└── README.md
```

## Example Questions

- Web Search Agent: "What are the latest developments in AI?"
- Finance Agent: "What is the current stock price of Tesla?"
- Agent Team: "Compare Apple and Microsoft stocks and provide recent news about both companies"

## License

MIT License - Feel free to use and modify this code for your purposes.