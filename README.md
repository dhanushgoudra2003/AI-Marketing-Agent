# 🚀 AI Marketing Intelligence Agent

An AI-powered multi-agent system that automatically generates **data-driven marketing strategies, campaign ideas, and growth plans** using LLMs and real-time insights.

---

## 🧠 Overview

This project leverages **CrewAI agents + LLMs (Ollama - Llama3)** to simulate a real marketing team:

* 📊 Market Analyst → Research & competitor analysis
* 🎯 Marketing Strategist → Strategy formulation
* 🚀 Growth Hacker → Growth plan & experiments
* ✍️ Content Creator → Campaign ideas & copies

The system produces a **complete marketing intelligence report + PDF output**.

---

## ✨ Features

* 🔍 Market & competitor analysis
* 🎯 Target audience understanding
* 📈 Marketing strategy generation
* 🚀 90-day growth plan
* 💡 Campaign idea generation
* ✍️ Marketing copy creation
* 📄 Automated PDF report generation
* ⚡ Multi-agent workflow using CrewAI

---

## 🏗️ Project Structure

```
AI-Marketing-Agent/
│
├── src/
│   └── marketing_posts/
│       ├── crew.py          # Agent + workflow logic
│       ├── main.py          # Entry point
│       ├── config/
│       │   ├── agents.yaml
│       │   ├── tasks.yaml
│
├── README.md
├── .gitignore
├── pyproject.toml
├── .env.example
```

---

## ⚙️ Tech Stack

* Python
* CrewAI
* Ollama (Llama3)
* Serper API (web search)
* ReportLab (PDF generation)

---

## 🚀 How to Run Locally

### 1. Clone the repo

```
git clone https://github.com/YOUR_USERNAME/AI-Marketing-Agent.git
cd AI-Marketing-Agent
```

---

### 2. Setup environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create `.env` file:

```
SERPER_API_KEY=your_api_key_here
```

---

### 5. Start Ollama

```
ollama serve
```

(Ensure `llama3` model is installed)

---

### 6. Run the project

```
python -m marketing_posts.main
```

---

## 📄 Output

The system generates:

* 📊 Marketing strategy report
* 💡 Campaign ideas
* ✍️ Ad copies
* 📈 Growth roadmap
* 📄 Exported PDF report

---

## 🎯 Example Use Case

Input:

```
Domain: aitool.com  
Product: AI-powered coding assistant
```

Output:

* Market insights
* Competitor analysis
* Growth strategy
* Campaign ideas
* Marketing copies

---

## 🔥 Future Improvements

* 🌐 Web UI (Streamlit / React)
* 📊 Dashboard for insights
* 📡 Live data integrations
* 🧠 Better ranking of campaigns
* ☁️ Cloud deployment


