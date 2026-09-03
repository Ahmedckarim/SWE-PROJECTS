# Software Engineering Journey

> **From beginner to professional Full-Stack + AI Engineer.**

This repository documents my journey from learning programming fundamentals to becoming a professional software engineer.

It serves as **proof of work**: a record of what I learn, what I build, the problems I solve, the engineering decisions I make, and how my skills develop over time.

---

## 🎯 Goal

My goal is to become a **Full-Stack + AI Engineer** capable of:

* Building production-quality software independently
* Designing and developing complete applications
* Building reliable backend systems and APIs
* Designing and working with databases
* Developing modern frontend applications
* Deploying and maintaining applications
* Applying software engineering principles
* Designing scalable systems
* Building and integrating AI/ML systems
* Qualifying for professional software engineering roles

---

# 🧭 Learning Roadmap

My learning path is progressive:

```text
Python
   ↓
Git & GitHub
   ↓
SQL & Databases
   ↓
Backend Development
   ↓
APIs & Authentication
   ↓
Linux
   ↓
Frontend Development
   ↓
Docker
   ↓
Cloud & Deployment
   ↓
System Design
   ↓
AI / Machine Learning
```

The objective is not simply to complete courses.

The objective is:

**Learn → Build → Document → Improve → Repeat**

---

# 📚 Roadmap & Progress
## Phase 1: Programming Fundamentals (3–5 weeks)

1. Python
    - ✅Variables
    - ✅Control flow
    - ✅Data types
    - ✅Functions
    - OOP
    - Modules, packages and packages managements
    - ✅Exceptions
    - ✅File handling
    - Virtual environments
    - Testing basics
    - Type hints (`typing` module) — you'll need this for FastAPI/Pydantic later
    - Decorators & context managers
    - Iterators/generators — needed for streaming data, LLM token streaming later
2. Git & GitHub
    - ✅commits
    - branches
    - pull requests
    - merge conflicts
    - GitHub workflow
    - Rebase vs merge
    - `.gitignore` / git hooks basics
3. Linux
    - terminal
    - file permissions
    - bash
    - ssh
    - package management
    - Process management (`ps`, `kill`, `systemd` basics) — needed once you're deploying
4. Math Basics
    - ☑️Algebra
    - Logic
    - Probability
    - Big-O intuition
    - Linear algebra basics (vectors, matrices, dot product)
    - Basic statistics (mean/variance/distributions)
    

---

## Phase 2: Computer Science (5–8 weeks)

### 1. Data Structures & Algorithms

Learn: Arrays, Strings, Linked Lists, Stacks, Queues, Heaps, Hash Tables, Trees, Graphs, Sorting, Searching, Recursion, Dynamic Programming

-  Tries — common in autocomplete/search features and some LLM tokenizer discussions

Practice: LeetCode, HackerRank

Goal: Solve ~150–250 problems.

**🛠 Projects:**

- Implement each core data structure from scratch (linked list, stack, queue, hash table, BST, graph) before relying on built-ins
- Build a simple autocomplete engine using a Trie
- Build a "six degrees of separation" search over a small graph (BFS/DFS practice)

---

## Phase 3: Databases (2–4 weeks)

### 1. SQL

Master: SELECT, JOIN, GROUP BY, HAVING, CTEs, Window Functions, Transactions, Indexes

### 2. PostgreSQL

Learn: Schema design, Constraints, Relationships, Normalization, Query optimization, Backup/restore

###  3. NoSQL & Specialized Stores

- Redis (caching, rate limiting, session store, pub/sub)
- MongoDB or similar (document store) — at least conceptually, many AI apps use it for unstructured data
- **Vector databases** (pgvector, Pinecone, Qdrant, or Weaviate) — this is the database layer your AI stack actually runs on (RAG, semantic search)

**🛠 Projects:**

- Design and normalize a schema for a real domain (e.g. library system, e-commerce store) then populate it and write increasingly complex queries (JOINs → window functions → CTEs)
- Add Redis caching in front of a slow query and measure the speedup
- Store a handful of text documents as embeddings in pgvector and run a similarity search query

---

## Phase 4: Backend Development (6–8 weeks)

### 1. REST APIs

Learn: HTTP, JSON, CRUD, REST principles, Status codes, Pagination, Validation

- GraphQL basics (just enough to know when it's the right tool)
- Idempotency & rate limiting

### 2. FastAPI

Learn: Routing, Models, Validation, Dependency Injection, Background Tasks, Middleware, Async programming

- WebSockets — needed for streaming LLM responses to a frontend
- Server-Sent Events (SSE) — the more common pattern for token streaming

### 3. Authentication

Learn: Sessions, Cookies, JWT, OAuth, Password hashing, Authorization, RBAC

- API key management — how you'll gate access to your own AI endpoints

### 4. Testing (deeper than Phase 1 basics)

- Unit tests (pytest), Integration tests, Mocking external APIs, Test coverage tools

### 5. Security Fundamentals

- OWASP Top 10 basics, SQL injection, XSS, CSRF
- Secrets management (env vars, vaults)
- Input sanitization — **especially important with LLMs** (prompt injection is the SQL-injection of the AI era)

**🛠 Projects:**

- Build a full CRUD REST API (e.g. a notes app or bookstore API) with Postgres + FastAPI, fully validated with Pydantic
- Add JWT-based auth + RBAC (admin vs regular user roles) to that API
- Add rate limiting (Redis-backed) and pagination to the endpoints
- Write a pytest suite with mocked external calls and get meaningful coverage
- Add a WebSocket or SSE endpoint that streams fake "typed" text, character by character (this is a direct rehearsal for streaming LLM output later)

---

## Phase 5: Frontend (4–6 weeks)

### 1. HTML / CSS / JavaScript

Learn: ES6+, DOM, Async/Await, Fetch API

### 2. React

Learn: Components, Hooks, Routing, Context, State Management

### 3. Next.js

Learn: App Router, Server Components, API Routes, SSR, SSG

-  Streaming UI patterns (rendering tokens as they arrive from an LLM)

**🛠 Projects:**

- A static portfolio site (HTML/CSS/JS only, no framework) — forces you to understand the fundamentals
- A React front-end for the CRUD API you built in Phase 4 (login, list, create, edit, delete)
- Rebuild that front-end in Next.js with the App Router, adding SSR for a public page and a protected dashboard route
- A chat-style UI component that renders streamed text token-by-token from your Phase 4 SSE endpoint

---

## Phase 6: DevOps (3–5 weeks)

### 1. Docker

Images, Containers, Docker Compose, Volumes, Networking

### 2. Deployment

Deploy to: Render, Railway, Fly.io, DigitalOcean, AWS (later)
Learn: Nginx, HTTPS, Environment variables, CI/CD (GitHub Actions)

###  3. Observability

- Logging (structured logs)
- Monitoring/metrics (Prometheus/Grafana or hosted equivalent)
- Error tracking (Sentry)
- **LLM-specific observability** (token usage, latency, cost tracking — LangSmith/Helicone)

**🛠 Projects:**

- Dockerize the Phase 4 API + Postgres + Redis with a single `docker-compose.yml`
- Set up a GitHub Actions pipeline that runs tests on every push and deploys on merge to `main`
- Deploy the full stack (API + frontend + DB) live on Render or Fly.io with HTTPS
- Add structured logging + Sentry error tracking + a basic Grafana dashboard to the deployed app

---

## Phase 7: System Design (3–4 weeks)

Do this right after Phase 4, while backend concepts are fresh.

Learn:

- Scalability basics: vertical vs horizontal scaling
- Load balancing
- Caching strategies (cache invalidation, CDN, Redis caching layers)
- Database scaling (replication, sharding, read replicas)
- Message queues (RabbitMQ, Kafka, or SQS) — async job processing, decoupling services
- Microservices vs monolith trade-offs
- API Gateway pattern
- Consistency models (CAP theorem, eventual consistency)
- Rate limiting & throttling design
- Designing for failure (circuit breakers, retries, timeouts, graceful degradation)
-  AI-specific system design: RAG pipelines, scalable LLM inference services, recommendation systems

Resources: "Designing Data-Intensive Applications" (book), ByteByteGo, System Design Primer (GitHub)

**🛠 Projects:**

- Add a message queue (e.g. Redis Queue or RabbitMQ) to your Phase 4 API for a slow task (e.g. sending emails, processing images) — turn a synchronous endpoint into an async job
- Write a full system design doc (with diagrams) for a URL shortener or rate limiter, then actually implement the rate limiter
- Write a system design doc specifically for a RAG-based Q&A service — this becomes your blueprint for Phase 8

---

## Phase 8: The AI Engineering Layer (6–10 weeks)

### Track A: Applied AI / LLM Engineering (do this first)

- How LLMs work conceptually (tokens, context windows, embeddings, attention)
- Prompt engineering fundamentals (few-shot, chain-of-thought, structured outputs)
- Using LLM APIs (OpenAI, Anthropic, open-source via Hugging Face/Ollama)
- **Retrieval-Augmented Generation (RAG)**: chunking strategies, embeddings, vector search, reranking
- **Agents & tool use**: function calling, agentic loops, orchestration (LangChain, LlamaIndex, or your own)
- Structured output / JSON mode, validation with Pydantic
- Fine-tuning basics (when to fine-tune vs prompt vs RAG)
- Evaluation of LLM outputs (automated evals, LLM-as-judge, golden datasets)
- Cost & latency optimization (caching, model selection, batching, streaming)
- Guardrails: prompt injection defense, output filtering, PII handling

### Track B: Core ML Foundations (optional, for deeper AI credibility)

- Python ML stack: NumPy, Pandas, scikit-learn
- Supervised vs unsupervised learning basics
- Neural network fundamentals (forward/backward pass, gradient descent)
- Basics of transformer architecture
- PyTorch basics
- MLOps basics: model versioning, experiment tracking (MLflow/W&B), model serving

**🛠 Projects:**

- Build a RAG chatbot over your own PDFs/notes, using the pgvector setup from Phase 3
- Wire that RAG chatbot into your Phase 4 FastAPI backend as a proper API endpoint, streamed to the Phase 5 frontend via SSE
- Build an agent that can call your own CRUD API's endpoints as "tools" (e.g. "add a task called X" via natural language)
- Write an eval script that scores your RAG chatbot's answers against a small golden dataset
- Track A capstone: take one of your earlier full-stack projects (e.g. the bookstore/notes app) and bolt on a real AI feature — semantic search, AI summarization, or an AI assistant — end to end, deployed
- (Track B, optional) Fine-tune a small open-source model on a toy dataset and serve it locally with Ollama
---

# 🛠️ Projects

Projects are the primary evidence of my practical progress.

I use projects to turn theoretical knowledge into engineering ability.

## Python Projects

### Completed / In Progress

* [✔️] Trivia Game
* [✔️] Random Password Generator
* [✔️] Calculator
* [✔️] To-Do List V1
* [✔️] Student Management System V1

Each project introduces new concepts and increases in complexity.



# 📈 Project Progression

My projects will increase in complexity as my engineering knowledge increases.

```text
Simple Scripts
      ↓
CLI Applications
      ↓
Structured Python Applications
      ↓
Database Applications
      ↓
REST APIs
      ↓
Full-Stack Applications
      ↓
Production Deployments
      ↓
Scalable Systems
      ↓
AI-Powered Applications
```

The objective is not to build as many projects as possible.

The objective is to progressively build **better, more realistic, and more complete software systems**.

---

# 🔬 Proof of Work

This repository is intended to provide evidence of my development as an engineer.

For important projects and milestones, I will document:

* What I learned
* What I built
* Why I built it
* Problems I encountered
* How I solved problems
* Technical decisions
* Bugs and debugging
* Architecture decisions
* Testing
* Improvements
* Deployment
* Lessons learned

### Learning Cycle

```text
Learn
  ↓
Practice
  ↓
Build
  ↓
Encounter Problems
  ↓
Debug & Research
  ↓
Solve
  ↓
Document
  ↓
Improve
  ↓
Build Something More Complex
```

The final code is only part of the proof.

The **engineering process is also part of the proof**.

---

# 🧠 Engineering Principles

Throughout this journey, I aim to develop the following habits:

* Understand before copying
* Build instead of only watching tutorials
* Read official documentation
* Practice problem solving
* Debug systematically
* Write maintainable code
* Use Git properly
* Test software
* Think about security
* Design before implementing complex systems
* Document important decisions
* Refactor when necessary
* Learn from failures
* Build progressively more difficult systems

---

# 📊 Current Direction

**Target Role:** Full-Stack + AI Engineer

**Current Focus:**

```text
Python Fundamentals
        ↓
Python Projects
        ↓
Git & GitHub
        ↓
SQL & Databases
        ↓
Backend Development
```

**Future Focus:**

```text
Backend
   +
Frontend
   +
Docker
   +
Cloud
   +
System Design
   +
AI / ML
```


# 📅 Progress Log

I will track meaningful milestones rather than simply counting hours studied.

```text
[✔️] Learned Python fundamentals
[✔️] Built first Python project
[✔️] Learned file handling
[✔️] Built multiple CLI applications
[✔️] Complete Student Management System CLI
[ ] Learn SQL
[ ] Build database-backed application
[ ] Learn FastAPI
[ ] Build REST API
[ ] Build full-stack application
[ ] Deploy application
[ ] Learn system design
[ ] Begin AI/ML
```

---

# 🎯 Long-Term Objective

I want to become an engineer capable of taking a real-world problem through the complete software development process:

```text
Problem
   ↓
Requirements
   ↓
Architecture
   ↓
Implementation
   ↓
Database
   ↓
Backend
   ↓
Frontend
   ↓
Testing
   ↓
Deployment
   ↓
Monitoring
   ↓
Scaling
   ↓
AI Integration
```

The ultimate objective is to build **working, maintainable, secure, scalable, and deployable software systems** that solve real problems.

---

## Status

**Journey:** In Progress 🚧

**Target:** Full-Stack + AI Engineer

**Approach:** Learn → Build → Document → Improve

> This repository is a record of the work required to become the engineer I want to be.
