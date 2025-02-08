# Minimal template for FastAPI, Supabase, SQLModel and Alembic

This is a minimal template for a FastAPI project with Supabase, SQLModel and Alembic.

## Features

- FastAPI for building APIs
- Supabase for authentication and database
- SQLModel for ORM
- Alembic for database versionning and migrations
- uv for dependency management

The project features a basic example of a bookmark application, supporting CRUD operations with Supabase authentication (including compatibility with Swagger's Auth).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/aipocket.git
    cd aipocket
    ```

2. Install UV:
    ```bash
    pip install uv
    ```
    You don't have to do that in a virtual environment, as UV is a standalone tool.
    UV will later on install the dependencies for you in a virtual environnement.

## Usage

1. Set up your environment variables for Supabase and database configuration or use an `.env` file based on the given example:
    ```bash
    cp .env.example .env
    ```

    Update the `.env` file with your Supabase URL, Supabase key, database URL, and database URL for migrations.

2. (Optional) In case you perform modifications to `models.py` (ie. modification to the DB scheme): Generate a new Alembic migration:
    ```bash
    uv run alembic revision --autogenerate -m "Your message here"
    ```

3. Run the database migrations:
    ```bash
    uv run alembic upgrade head
    ```

4. Start the FastAPI server:
    ```bash
    uv run uvicorn app.main:app --reload --reload-dir app
    ```
    At the first run, UV will create a virtual environment and install the dependencies inside it.

5. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
