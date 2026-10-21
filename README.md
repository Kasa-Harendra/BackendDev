# Backend Development Tutorial

A beginner-friendly FastAPI backend tutorial covering RESTful API fundamentals, request handling, status codes, and endpoint routing.

---

## 🚀 Features

- **FastAPI Framework**: High performance, easy-to-learn Python web framework.
- **RESTful Endpoints**:
  - `GET /`: Health check / server status.
  - `POST /todos`: Create a new todo task.
  - `GET /todos`: Retrieve all todo tasks.
  - `GET /todos/{id}`: Retrieve a specific todo by ID.
- **Lecture Boards**: Visual diagrams (`.excalidraw`) in `lecture-boards/` explaining API design and architectural concepts.

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
uvicorn main:app --reload
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
├── .gitignore
├── README.md
├── main.py              # FastAPI application & route handlers
└── lecture-boards/      # Excalidraw concept & lecture architecture diagrams
```
