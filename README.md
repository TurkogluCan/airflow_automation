# Airflow Automation

This project provides a local Apache Airflow environment setup using Docker Compose. It allows for easy development and testing of Airflow DAGs.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd airflow_automation
    ```

2.  **Initialize the environment:**
    The project is configured to use the official Apache Airflow Docker image.

3.  **Start the services:**
    Run the following command to start all Airflow services (Webserver, Scheduler, Triggerer, etc.) in detached mode:
    ```bash
    docker-compose up -d
    ```
    *Note: The first run might take a few minutes as it pulls images and initializes the database.*

4.  **Access Airflow UI:**
    Once the services are running, access the Airflow web interface at:
    [http://localhost:8080](http://localhost:8080)

    - **Username:** `airflow`
    - **Password:** `airflow`

5.  **Stop the services:**
    To stop and remove the containers, networks, and volumes:
    ```bash
    docker-compose down
    ```

## Project Structure

- **`dags/`**: Contains your Airflow Directed Acyclic Graphs (DAGs).
    - `our_first_dag.py`: An example DAG (`our_first_dag_V2`) demonstrating simple `BashOperator` tasks.
- **`docker-compose.yaml`**: Defines the services (Postgres, Redis, Airflow components) required to run Airflow locally.
- **`config/`**: Custom configuration files (mounted to `/opt/airflow/config`).
- **`logs/`**: Airflow logs (mounted to `/opt/airflow/logs`).
- **`plugins/`**: Custom plugins (mounted to `/opt/airflow/plugins`).

## Example DAGs

### `our_first_dag_V2`
This is a sample DAG located in `dags/our_first_dag.py`.
- **Schedule:** Runs daily (`@daily`).
- **Tasks:** Executes three simple bash echo commands.
- **Structure:** `task1` runs in parallel with `task2` and `task3` (visualized as `task1 >> [task2, task3]`).

## Configuration
The `docker-compose.yaml` file is set up for local development:
- **Executor:** `LocalExecutor`
- **Database:** PostgreSQL
- **Auth Manager:** FAB (Flask App Builder)
