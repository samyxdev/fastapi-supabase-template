# Minimal template for FastAPI, Supabase, SQLModel and Alembic

This is a minimal template for a FastAPI project with Supabase, SQLModel and Alembic.

## Features

- FastAPI for building APIs
- Supabase for authentication and database
- SQLModel for ORM
- Alembic for database migrations
- uv for dependency management

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aipocket.git
    cd aipocket
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set up your environment variables for Supabase and database configuration or use an `.env` file based on the given example:
    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your Supabase URL, Supabase key, database URL, and database URL for migrations.

2. Run the database migrations:
    ```bash
    alembic upgrade head
    ```

3. Start the FastAPI server:
    ```bash
    fastapi dev app/main.py
    ```

4. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
