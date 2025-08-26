# task_management_assignment

A small task management service where users can create projects and tasks. Each project can have multiple tasks, and tasks can be marked as pending, in-progress, or completed.

## Setup Instructions

### Prerequisites

-   Docker and Docker Compose installed
-   Node.js and npm installed (for building the frontend)

### Steps

1. **Build the Frontend**

    - Navigate to the `frontend_app` directory:
        ```
        cd frontend_app
        ```
    - Install dependencies:
        ```
        npm install
        ```
    - Build the project (creates the `dist` folder):
        ```
        npm run build
        ```

2. **Create Backend Environment File**

    - In the `backend_app` folder, create a `.env` file with required environment variables, for example:
        ```
        MONGO_DB=your_db_name
        JWT_SECRET=your_jwt_secret
        ```
    - You can adjust these values as needed.

3. **Build Docker Containers**

    - From the project root directory, run:
        ```
        docker-compose build
        ```

4. **Start the Application**

    - Run the containers:
        ```
        docker-compose up
        ```

5. **Access the Application**
    - Open your browser and go to: [http://127.0.0.1/](http://127.0.0.1/)

## API Endpoints Overview

Below is a summary of the main API endpoints exposed by the backend:

### User Endpoints (`/api/user`)

-   `POST /register` — Register a new user
-   `POST /login` — Login and receive JWT token

### Project Endpoints (`/api/project`)

-   `POST /` — Create a new project (requires authentication)
-   `GET /` — List all projects (requires authentication)
-   `PUT /{project_id}` — Update a project (requires authentication)
-   `DELETE /{project_id}` — Delete a project (requires authentication, only creator)

### Task Endpoints (`/api/task`)

-   `POST /` — Create a new task (requires authentication)
-   `GET /` — List all tasks (requires authentication)
-   `PATCH /{task_id}/status` — Update status of a task (requires authentication)
-   `PUT /{task_id}` — Update a task (requires authentication)

For detailed request/response models and to try out the endpoints interactively, visit the [Swagger UI](http://127.0.0.1/api/docs) after starting the application.

### Additional Notes

-   Backend logs can be viewed in the Docker container output.
-   If you change environment variables, rebuild the containers.
-   MongoDB data is persisted in the `mongo_data` volume.
-   The backend API is available at `/api` (e.g., `http://127.0.0.1/api`).
-   Make sure ports `8000` (backend), `27017` (MongoDB), and `80` (frontend/nginx) are available on your system.
-   **API Documentation:**  
    You can access the interactive API docs (Swagger UI) at [http://127.0.0.1/api/docs](http://127.0.0.1/api/docs)
