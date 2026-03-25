📚 Academic Research Agent

An Agentic AI-based research assistant that can plan, retrieve, summarize, and explain academic content from documents like PDFs. This system demonstrates multi-agent orchestration with memory and reasoning capabilities.

🚀 Features
🧠 Planner Agent – Breaks down user queries into structured tasks
📄 Retriever Agent – Extracts relevant content from PDFs
✍️ Summarizer Agent – Generates concise summaries
💡 Explainer Agent – Provides easy-to-understand explanations
🔁 Recursive Agent – Expands answers for deeper understanding
🧩 Memory Module – Stores and retrieves similar past queries
🏗️ Project Structure
agentic_project/
│── agents/
│   ├── planner_agent.py
│   ├── retrieval_agent.py
│   ├── summarizer_agent.py
│   ├── explainer_agent.py
│   ├── recursive_agent.py
│
│── memory/
│   └── memory_manager.py
│
│── tools/
│   └── pdf_loader.py
│
│── models/
│   └── openai_model.py
│
│── orchestrator.py
│── app.py
│── sample_paper.pdf
│── README.md
⚙️ Installation
Clone the repository:
git clone https://github.com/Vamsikrishnasatvik/Academic-Research-Agent.git
cd Academic-Research-Agent
Install dependencies:
pip install -r requirements.txt
Set your OpenAI API Key:
setx OPENAI_API_KEY "your_api_key_here"
▶️ Usage

Run the application:

python app.py

Example query:

"Explain the concept of Agentic AI systems"
🔄 Workflow
User enters a query
Planner agent creates a task plan
Retriever fetches relevant content from PDF
Summarizer condenses the information
Explainer simplifies the concept
Recursive agent expands details if needed
Memory stores the query for future reuse
🧠 Technologies Used
Python 🐍
OpenAI API 🤖
PDF Processing
Agent-based Architecture
📌 Example Use Cases
Research paper analysis
Academic learning assistant
Literature review automation
Concept explanation system
📈 Future Improvements
Web search integration 🌐
Multi-document support 📚
UI (Streamlit / Web App) 🎨
Vector database memory (FAISS) 🧠
Citation generation 📑
🤝 Contributing

Feel free to fork this repository and contribute!

📜 License

This project is for educational purpose.
