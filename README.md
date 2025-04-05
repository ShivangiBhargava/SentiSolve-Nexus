"SentiSolve Nexus"

An intelligent multi-agent framework for AI-driven support automation.

✅Features
- Summarization via LLM
- Root cause classification (XGBoost)
- Resolution retrieval via vector search
- ETA prediction
- Routing + Feedback loops

✅Tech Stack
- Ollama (LLM)
- FastAPI
- FAISS / Chroma (optional)
- Scikit-learn, LangChain

📁 Project Folder Structure:

```bash
sentisolve-nexus/
├── agents/
│   ├── summarizer_agent.py
│   ├── vectorizer_agent.py
│   ├── root_cause_classifier.py
│   ├── resolution_recommender.py
│   ├── router.py
│   ├── eta_predictor.py
│   └── feedback_agent.py
├── app/
│   ├── api.py
│   └── frontend.py
├── data/
│   ├── Historical_ticket_data.csv
│   └── issues/
│       ├── Account Synchronization Bug.txt
│       ├── Software Installation Failure.txt
│       ├── Payment Gateway Integration Failure.txt
│       ├── Network Connectivity Issue.txt
│       └── Device Compatibility Error.txt
├── models/
│   ├── root_cause_model.pkl
│   └── eta_model.pkl
├── vector_store/
│   └── vector_index.pkl
├── main.py
├── requirements.txt
├── run_app.sh
└── README.md

``` 
Run the agents:
```bash
python main.py
