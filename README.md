# Backend Development Tutorial

A beginner-friendly backend engineering tutorial covering RESTful API fundamentals, system architecture, request handling, status codes, and hands-on FastAPI implementation.

---

## 📚 Lecture Sessions (Parts)

Each part serves as a dedicated lecture session featuring interactive visual architecture boards, hands-on source code, and concrete learning outcomes:

| Part / Session | Topic | Lecture Board | Actual Code | Learning Outcomes |
| :--- | :--- | :--- | :--- | :--- |
| **Part 1** | **API Architecture & HTTP Fundamentals** | [1.excalidraw](parts/part-1/lecture_boards/1.excalidraw) | [main.py](parts/part-1/src/main.py) | • **Client-Server Architecture**: Multi-tier flow (Client ➔ API Gateway / Reverse Proxy ➔ Application Server ➔ Database / Cache).<br>• **URL Anatomy**: Base URL, Route, Path Parameters (`/users/42` for identity), Query Parameters (`?limit=5` for filtering/pagination), and Anchors.<br>• **HTTP Protocol Deep Dive**: Request/Response lines, Header metadata (Auth, Content-Type, Caching), and JSON Payloads.<br>• **Data Formats & Validation**: Comparing JSON, XML, YAML, and understanding data contracts & schema validation.<br>• **HTTP Methods & Semantics**: GET, POST, PUT, DELETE, PATCH; Safe vs. Idempotent operations.<br>• **Status Code Taxonomy**: 1xx (Informational), 2xx (Success), 3xx (Redirection), 4xx (Client Errors), 5xx (Server Errors).<br>• **Architectural Paradigms**: REST, GraphQL, gRPC, WebSockets, and the 6 REST constraints (Statelessness, Uniform Interface, Layered System, etc.). |
| **Part 2** | **REST API Design & Implementation (To-Do App)** | [todo-api-lecture.excalidraw](parts/part-2/lecture-boards/todo-api-lecture.excalidraw) | [main.py](parts/part-2/src/main.py) | • **API Mental Model**: Real-world Restaurant Analogy (Client = Customer, API Server = Waiter, Storage = Kitchen).<br>• **Resource Modeling**: Designing a `Task` entity with `id`, `name`, `description`, and `done` state.<br>• **Sequence Diagrams**: Visualized request-response lifecycle for all 5 CRUD operations (POST, GET list, GET single, PUT, DELETE).<br>• **FastAPI Endpoint Construction**: Writing `POST /todos` (201 Created), `GET /todos` (200 OK), and `GET /todos/{id}` with Path Parameters.<br>• **Error Handling & Status Codes**: Using `HTTPException` and `JSONResponse` to return appropriate client responses (e.g., 400 Bad Request, 404 Not Found).<br>• **Interactive Documentation**: Verifying and testing endpoints using automated Swagger UI (`/docs`) and ReDoc (`/redoc`). |

---

## 🎯 Lecture Breakdown & Deep Dive

### 🔹 Part 1: API Development Architecture & Core Concepts
- **Lecture Board**: [`parts/part-1/lecture_boards/1.excalidraw`](parts/part-1/lecture_boards/1.excalidraw)
- **Source Code**: [`parts/part-1/src/main.py`](parts/part-1/src/main.py)
- **Focus**: Establishing a solid mental model of web protocols and architectural design before writing server code.
- **Key Concepts Covered**:
  - The multi-tier client-server lifecycle and separation of concerns.
  - Deconstructing URLs: Host, port, path parameters vs. query parameters.
  - Anatomy of HTTP/1.1 and HTTP/2 requests and responses.
  - Serialization standards: JSON vs. XML vs. YAML.
  - Data contracts, payload validation, and defensive programming.
  - HTTP method safety and idempotency rules (GET/PUT vs. POST).
  - Categorizing HTTP status codes (200, 201, 204, 400, 401, 403, 404, 500, 502, 503).
  - Comparing API paradigms: REST, GraphQL, gRPC, WebSockets, and Webhooks.

### 🔹 Part 2: RESTful To-Do API Design & Implementation
- **Lecture Board**: [`parts/part-2/lecture-boards/todo-api-lecture.excalidraw`](parts/part-2/lecture-boards/todo-api-lecture.excalidraw)
- **Source Code**: [`parts/part-2/src/main.py`](parts/part-2/src/main.py) (also mirrored at [`main.py`](main.py))
- **Focus**: Translating architectural concepts and sequence diagrams into a working FastAPI application.
- **Key Concepts Covered**:
  - Designing clean RESTful URL paths using nouns (`/todos`, `/todos/{id}`).
  - Implementing CRUD endpoints:
    - `POST /todos`: Parse request body, auto-generate sequential IDs, default task state, return `201 Created`.
    - `GET /todos`: Return array of existing tasks with `200 OK`.
    - `GET /todos/{id}`: Parse URL path parameter, search tasks, return `200 OK` or raise `404 Not Found`.
    - `PUT /todos/{id}` & `DELETE /todos/{id}`: Updating and removing resource state.
  - Utilizing FastAPI's `Request`, `HTTPException`, `status`, and `JSONResponse`.
  - Testing APIs interactively with Swagger UI.

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

