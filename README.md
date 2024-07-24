# Trip Planner Application

## Overview

The Trip Planner Application is a web-based tool designed to help users plan their travel routes efficiently. Built using a combination of Python and JavaScript technologies, this application allows users to manage their trip stops, view available airports, and calculate distances between locations. The project includes a backend API implemented with Flask and a frontend built with React.

## Features

- **User Authentication:** Secure user login and registration using JWT (JSON Web Tokens).
- **Airport Data Management:** Access and manage a list of airports with their geographical coordinates.
- **Trip Management:** Add, remove, and view stops on your trip, with real-time updates.
- **Distance Calculation:** Calculate distances between airports using Haversine formula.
- **Graph-Based Routing:** Find the shortest path between airports using graph algorithms.
- **Responsive Design:** Modern and user-friendly interface with React.

## Technologies Used

- **Backend:**
  - Python
  - Flask
  - MongoDB
  - Flask-RESTful
  - `python-dotenv` for environment management

- **Frontend:**
  - React
  - Axios for HTTP requests
  - Bootstrap for styling
  - React Router for navigation

- **DevOps:**
  - Environment configuration using `.env` files
  - `concurrently` for running backend and frontend concurrently during development

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone [this repository]
   ```

2. **Backend Setup:**

   Navigate to the `backend` directory:

   ```bash
   cd trip-planner/backend
   ```

   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install backend dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Create a `.env` file for environment variables and configure it as needed.

   Run the Flask application:

   ```bash
   python app.py
   ```

3. **Frontend Setup:**

   Navigate to the `frontend` directory:

   ```bash
   cd trip-planner/frontend
   ```

   Install frontend dependencies:

   ```bash
   npm install
   ```

   Start the React application:

   ```bash
   npm start
   ```

4. **Running Both Backend and Frontend Concurrently:**

   Use the `concurrently` package to run both servers:

   ```bash
   npm run start
   ```

   This will start both the backend and frontend applications simultaneously.

## Usage

- Open your web browser and navigate to `http://localhost:3000` to access the frontend.
- The backend API will be running on `http://localhost:5000`.

