# FastAPI Sample REST API

This project is a simple FastAPI application that exposes a REST endpoint `GET /items` returning a JSON list of sample items.

## Features
- FastAPI framework for building APIs.
- Built-in OpenAPI support for API documentation.
- Dockerized application for easy deployment.

## Getting Started

### Build and Run Locally

1. Build the Docker image:
   ```bash
   docker build -t fastapi-sample .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 fastapi-sample
   ```

   **Note:** Ensure the Dockerfile installs all dependencies listed in requirements.txt, including uvicorn, and sets the correct CMD to run the FastAPI application.

3. Access the API:
   - Visit `http://localhost:8000/items` to see the sample items.
   - Open `http://localhost:8000/docs` for the automatically generated API documentation.

## Requirements
- Docker
- Python 3.9+

## Development
To run the application locally without Docker:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the application:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
