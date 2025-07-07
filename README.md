
# Movie Explorer Platform

The **Movie Explorer Platform** is a full-stack application designed to explore movies, actors, directors, and genres. The platform provides filtering, searching, and detailed movie information features. Built using **FastAPI** for the backend and **React** with **Vite** for the frontend, it is a fully dockerized solution for easy deployment.

## Project Overview

The platform allows users to:

* Search and filter movies, actors, directors, and genres.
* View detailed movie information by clicking on movie cards.

## Table of Contents

* [Technologies Used](#technologies-used)
* [Project Structure](#project-structure)
* [Installation](#installation)
* [Setup Backend](#setup-backend)
* [Setup Frontend](#setup-frontend)
* [Running the Application](#running-the-application)
* [Testing](#testing)
* [Deployment](#deployment)

## Technologies Used

* **Backend**: FastAPI
* **Frontend**: React.js, Vite
* **Database**: SQLite
* **Containerization**: Docker
* **ORM**: SQLAlchemy

## Project Structure

The project is divided into two main parts: the backend and frontend.

### Backend Structure

```
movie_explorer/
│
├── backend/
│   ├── app/
│   │   ├── main.py            # FastAPI (or Flask) app entry point
│   │   ├── models.py          # Database models using SQLAlchemy
│   │   ├── api/               # API endpoints
│   │   ├── services/          # Application business logic
│   │   └── utils/             # Helper functions and utilities
│   ├── Dockerfile             # Dockerfile to containerize backend
│   ├── requirements.txt       # Python dependencies
│   ├── seed_data.py           # to load sample data in to db

```

### Frontend Structure

```
movie_explorer/
│
├── frontend/
│   ├── src/
│   │   ├── components/        # Reusable UI components (buttons, cards, etc.)
│   │   ├── pages/             # React pages for various views (Home, Movie Details, etc.)
│   │   ├── hooks/             # Custom React hooks
│   │   └── services/          # API calls and logic to interact with the backend
│   ├── public/                # Static files like images and icons
│   ├── Dockerfile             # Dockerfile to containerize frontend
│   ├── package.json           # Frontend dependencies
│   ├── vite.config.js         # Vite configuration file
```

### Docker

```
movie_explorer/
│
├── docker-compose.yml         # Docker Compose file to run both frontend and backend together
```

## Installation

### Prerequisites

* Docker and Docker Compose must be installed on your machine.

### Backend Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Madhun86/movie_explorer.git
   cd movie_explorer
   ```

2. Navigate to the backend folder:

   ```bash
   cd backend
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. run seed_data.py to load sample data into DB
   ```
   python seed_data.py
   ```

### Frontend Installation

1. Navigate to the frontend folder:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

## Running the Application

### Running the Backend

1. If you are not using Docker, you can run the backend locally:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Alternatively, run the backend using Docker:

   ```bash
   docker-compose up backend
   ```

### Running the Frontend

1. If you are not using Docker, you can run the frontend locally:

   ```bash
   npm run dev
   ```

2. Alternatively, run the frontend using Docker:

   ```bash
   docker-compose up frontend
   ```

### Running Both Frontend and Backend Using Docker

To run both the frontend and backend together with Docker Compose:

```bash
docker-compose up --build
```

This will start both services in the background, and you can access the application at `http://localhost:5173` for the frontend and `http://localhost:8000` for the backend.

## Testing

To run tests for the backend, you can use:

```bash
pytest
```

## Deployment

### Docker Deployment

1. Build the Docker images for the backend and frontend:

   ```bash
   docker-compose build
   ```
