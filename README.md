# HireGraph - LangGraph Smart Hiring Assistant

HireGraph is a LangGraph-powered hiring assistant that:
- Reads resumes and job descriptions
- Classifies candidate seniority
- Scores candidates across multiple dimensions
- Generates explainable hiring recommendations
- Drafts personalized emails
- Supports human-in-the-loop review
- Implements retries, recovery loops, saga compensation, and orchestration patterns

---

---

# Folder structure

hiregraph/
│
├── README.md
├── requirements.txt
├── .env.example
├── main.py
│
├── graph_out/
│   └── graph.png
│
├── sample_data/
│   ├── jds/
│   │   ├── jd_senior_backend.md
│   │   └── jd_junior_data.md
│   │
│   ├── resumes/
│   │   ├── resume_priya.md
│   │   ├── resume_eitan.md
│   │   └── resume_mira.md
│   │
│   └── expected_outcomes.md
│
├── api/
│   └── server.py
│
├── ui/
│   └── app.py
│
├── notebooks/
│   └── walkthrough.ipynb
│
├── tests/
│   ├── test_state.py
│   ├── test_nodes.py
│   └── test_e2e.py
│
└── src/
    └── hiregraph/
        │
        ├── graph.py
        ├── state.py
        ├── llm.py
        ├── schemas.py
        │
        ├── nodes/
        │   ├── classify.txt
        │   ├── scoring.txt
        │   ├── email.txt
        │   └── critique.txt
        │
        ├── nodes/
        │   ├── ingest.py
        │   ├── classify.py
        │   ├── planning.py
        │   ├── orchestrator.py
        │   ├── skill_worker.py
        │   ├── scoring.py
        │   ├── research_agent.py
        │   ├── decision.py
        │   ├── human_review.py
        │   ├── email.py
        │   ├── rejection.py
        │   ├── retry_nodes.py
        │   ├── compensation.py
        │   ├── recovery.py
        │   └── finalize.py
        │
        ├── tools/
        │   ├── tavily_search.py
        │   └── github_lookup.py
        │
        └── services/
            ├── ats_service.py
            ├── email_service.py
            └── mock_services.py


---

resume + jd
   ↓
ingest
   ↓
classify seniority
   ↓
plan required skills
   ↓
ORCHESTRATE workers (Send)
   ↓
PARALLEL scorers (experience, education, signal, research)
   ↓
aggregate scores
   ↓
recommendation (advance / reject / borderline)
   ↓
IF borderline → interrupt (human review)
   ↓
email draft
   ↓
critic loop (retry up to 3)
   ↓
send email + ATS
   ↓
finalize


---

# Features

- LangGraph orchestration
- TypedDict state
- Structured outputs
- Parallel scoring
- Orchestrator-worker pattern
- Evaluator-optimizer loop
- Tool calling
- Retry policies
- Human approval with interrupt()
- Saga compensation handling
- Graph visualization

---

# Setup

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Create `.env`

```env
OPENAI_API_KEY=your_key
TAVILY_API_KEY=your_key
HIREGRAPH_USE_MOCKS=true
```

Run:

```bash
python main.py
```

---

# Architecture

See `graph_out/graph.png`

---

# Required Assignment Patterns

| Pattern | Implemented |
|---|---|
| TypedDict State | ✅ |
| Command Routing | ✅ |
| RetryPolicy | ✅ |
| LLM Recovery Loop | ✅ |
| interrupt() | ✅ |
| Saga Compensation | ✅ |
| Structured Output | ✅ |
| Tool Calling | ✅ |
| Parallelization | ✅ |
| Orchestrator Workers | ✅ |
| Evaluator Optimizer | ✅ |
