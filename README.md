# FastAPI Task Management Project

This is a simple FastAPI project for managing tasks. It provides CRUD (Create, Read, Update, Delete) operations for tasks.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Install dependencies:

    ```bash
    pip install -r requirements.txt

3. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
   

# Endpoints
## I. Create Task
URL: /tasks/ <br>
Method: POST <br>
Description: Create a new task. <br>
Request Body: <br>

    {
      "id": <int>,
      "title": <string>,
      "description": <string>,
      "completed": <boolean>
    }

Example:

    curl -X POST "http://localhost:8000/tasks/" -H "Content-Type: application/json" -d '{"id": 1, "title": "Complete assignment", "description": "Finish the FastAPI project", "completed": false}'

## II. Read Tasks
URL: /tasks/ <br>
Method: GET <br>
Description: Retrieve all tasks. <br>
Example: <br>

    curl -X GET "http://localhost:8000/tasks/"
## III. Update Task
URL: /tasks/{task_id} <br>
Method: PUT <br>
Description: Update an existing task. <br>
Request Body: <br>

    {
      "id": <int>,
      "title": <string>,
      "description": <string>,
      "completed": <boolean>
    }

Example:

    curl -X PUT "http://localhost:8000/tasks/0" -H "Content-Type: application/json" -d '{"id": 0, "title": "Updated task", "description": "Updated description", "completed": true}'


## IV. Delete Task
URL: /tasks/{task_id} <br>
Method: DELETE <br>
Description: Delete an existing task. <br>
Example: <br>

    curl -X DELETE "http://localhost:8000/tasks/0"



# Contributing
Contributions are welcome! If you have suggestions or encounter issues, please open an issue or submit a pull request.
