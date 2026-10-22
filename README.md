# Backend Development Tutorial

A beginner-friendly backend engineering tutorial covering RESTful API fundamentals, system architecture, request handling, status codes, and hands-on FastAPI implementation.

---

## 📚 Lecture Sessions (Parts)

Each part serves as a dedicated lecture session featuring interactive visual architecture boards, hands-on source code, and concrete learning outcomes:

| Part / Session | Topic | Lecture Board | Actual Code | Learning Outcomes |
| :--- | :--- | :--- | :--- | :--- |
| **Part 1** | **API Architecture & HTTP Fundamentals** | [1.excalidraw](parts/part-1/lecture_boards/1.excalidraw) | [main.py](parts/part-1/src/main.py) | • Client-Server Architecture<br>• URL Anatomy (Path vs Query Params)<br>• HTTP Protocol & Headers<br>• Data Formats (JSON, YAML, XML)<br>• Data Contracts & Validation<br>• HTTP Methods & Idempotency<br>• HTTP Status Codes (1xx–5xx)<br>• REST Architectural Constraints |
| **Part 2** | **REST API Design & Implementation (To-Do App)** | [todo-api-lecture.excalidraw](parts/part-2/lecture-boards/todo-api-lecture.excalidraw) | [main.py](parts/part-2/src/main.py) | • Request-Response Mental Model<br>• Task Resource Modeling<br>• CRUD Sequence Diagrams<br>• FastAPI Routing (`POST`, `GET`, `GET /{id}`)<br>• Status Codes & `HTTPException`<br>• Interactive Swagger UI Docs (`/docs`) |

---

## 🎯 Lecture Breakdown & Deep Dive

### 🔹 Part 1: API Development Architecture & Core Concepts
- **Lecture Board**: [`parts/part-1/lecture_boards/1.excalidraw`](parts/part-1/lecture_boards/1.excalidraw)
- **Source Code**: [`parts/part-1/src/main.py`](parts/part-1/src/main.py)
- **Learning Outcomes**:
  - Client-Server Architecture & Multi-tier Flow
  - URL Anatomy (Host, Route, Path & Query Parameters)
  - HTTP Protocol, Headers & Payloads
  - Serialization Formats (JSON, XML, YAML)
  - Data Contracts & Schema Validation
  - HTTP Method Semantics & Idempotency
  - Status Code Classifications (1xx–5xx)
  - REST Constraints vs GraphQL / gRPC / WebSockets

### 🔹 Part 2: RESTful To-Do API Design & Implementation
- **Lecture Board**: [`parts/part-2/lecture-boards/todo-api-lecture.excalidraw`](parts/part-2/lecture-boards/todo-api-lecture.excalidraw)
- **Source Code**: [`parts/part-2/src/main.py`](parts/part-2/src/main.py) (also mirrored at [`main.py`](main.py))
- **Learning Outcomes**:
  - Request-Response Mental Model (Restaurant Analogy)
  - Task Resource Modeling (`id`, `name`, `description`, `done`)
  - CRUD Sequence Diagrams (POST, GET, PUT, DELETE)
  - FastAPI Route Handlers & URL Nouns
  - Status Codes (`200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`)
  - Error Handling with `HTTPException` & `JSONResponse`
  - Interactive API Testing (Swagger UI & ReDoc)

---

## 🚀 Features

- **FastAPI Framework**: High performance, easy-to-learn Python web framework.
- **RESTful Endpoints**:
  - `GET /`: Health check / server status.
  - `POST /todos`: Create a new todo task.
  - `GET /todos`: Retrieve all todo tasks.
  - `GET /todos/{id}`: Retrieve a specific todo by ID.
- **Visual Lecture Boards**: Comprehensive Excalidraw diagrams detailing architecture, network flows, and endpoint sequence diagrams.

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.9+
- `pip` or virtual environment manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kasa-Harendra/BackendDev.git
   cd BackendDev
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Server

Start the development server with live reload:
```bash
# Run root application:
uvicorn main:app --reload

# Or run Part 2 directly:
uvicorn parts.part-2.src.main:app --reload
```

The API will be accessible at:
- **API Base URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📖 API Reference

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Server health check | `200 OK` |
| `POST` | `/todos` | Create a new todo item | `201 Created` |
| `GET` | `/todos` | Fetch list of all todos | `200 OK` |
| `GET` | `/todos/{id}` | Fetch a single todo by ID | `200 OK` / `404 Not Found` |

---

## 📂 Project Structure

```
.
├── README.md
├── main.py                  # Main application entry point (FastAPI To-Do API)
├── parts/
│   ├── part-1/              # Lecture Session 1: Architecture & Core Concepts
│   │   ├── lecture_boards/  # Excalidraw visual diagrams (1.excalidraw)
│   │   └── src/             # Session source code (main.py)
│   └── part-2/              # Lecture Session 2: RESTful To-Do API Design & Implementation
│       ├── lecture-boards/  # Excalidraw sequence diagrams (todo-api-lecture.excalidraw)
│       └── src/             # FastAPI implementation (main.py)
├── media/                   # Assets (images, texts, videos)
└── anim/                    # Manim automated animation pipeline
```

