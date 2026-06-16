# AI Marketing Strategy Generator

This project uses CrewAI agents to research a company/product and generate a practical marketing intelligence report. It can be used from the terminal or through a small Streamlit interface.

## What It Generates

Each run creates a timestamped folder in `reports/` containing:

- `marketing_report.pdf` - formatted PDF report
- `report.md` - raw AI-generated report text
- `report_data.json` - parsed report data and artifact paths

The report is built from the agent output instead of static placeholder text.

## Agent Workflow

The CrewAI pipeline runs these tasks in sequence:

1. Research the company, market, competitors, and opportunities.
2. Identify the product's target audience and pain points.
3. Create positioning, messaging, tactics, channels, and KPIs.
4. Build a 90-day growth plan.
5. Generate campaign ideas.
6. Write marketing copy.
7. Compile the final marketing intelligence report.

## Setup

Copy the example environment file:

```powershell
Copy-Item .env.example .env
```

Update `.env` with your Serper API key:

```env
SERPER_API_KEY=your_serper_key
OPENAI_API_KEY=ollama
OPENAI_MODEL_NAME=ollama/llama3.1
OLLAMA_BASE_URL=http://127.0.0.1:11434
```

The current default model is local Ollama `llama3.1`, because the research agent needs a model that supports tool calls. Make sure Ollama is running and the model is installed:

```powershell
ollama pull llama3.1
ollama serve
```

Install dependencies with Poetry:

```powershell
poetry install
```

Or with uv:

```powershell
uv sync
```

## Run From Terminal

```powershell
poetry run marketing_posts
```

You will be prompted for:

- company domain
- product/project description

When generation finishes, the terminal prints the generated report and the paths to the saved PDF, Markdown, and JSON files.

## Run The Web UI

```powershell
poetry run streamlit run src/marketing_posts/app.py
```

The UI lets you enter the same inputs, preview the generated report, and download the output files.

## Main Files

- `src/marketing_posts/main.py` - CLI, validation, artifact generation, PDF builder
- `src/marketing_posts/app.py` - Streamlit web interface
- `src/marketing_posts/crew.py` - CrewAI agents and task pipeline
- `src/marketing_posts/config/agents.yaml` - agent definitions
- `src/marketing_posts/config/tasks.yaml` - task prompts

## Notes

- The Serper API is used during research.
- Ollama is used for local LLM calls when `OPENAI_MODEL_NAME` starts with `ollama/`.
- PDF generation is local and does not call external APIs.
