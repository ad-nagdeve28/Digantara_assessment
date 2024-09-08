"# Digantara_assessment" 

# Job Scheduler Microservice

This project implements a Python-based microservice that schedules jobs using Flask, SQLAlchemy, and APScheduler.

## Features
- List all jobs
- Retrieve a specific job by ID
- Schedule a new job with customizable schedule settings

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/ad-nagdeve28/Digantara_assessment.git
    cd digantara
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

5. API Endpoints:
    - `GET /jobs`: List all scheduled jobs.
    - `GET /jobs/:id`: Get details of a specific job.
    - `POST /jobs`: Create a new job. Example JSON body:
    ```json
    {
        "name": "Job Name",
        "schedule": "* * * * *"  # Cron expression
    }
    ```

## Scaling
- **Horizontal scaling**: Multiple instances of the app can be run and load-balanced to handle higher traffic.
- **Database scaling**: Use distributed databases like PostgreSQL or MySQL for larger datasets.
- **API scaling**: Implement API rate-limiting, caching (e.g., Redis), and consider partitioning to handle high request rates.

