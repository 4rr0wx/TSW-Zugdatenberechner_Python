# Flet app

Flet app using Flet extension.

This version allows entering basic train data to calculate the PZB train type
based on the brake ratio.

To run the app:

1. Install dependencies from pyproject.toml:

```
poetry install
```

2. Build app:

```
poetry run flet build macos -v
```

3. Run app:

```
poetry run flet run
```

## Docker

Build the Docker image and run the app:

```
docker build -t tsw-zugdatenberechner .
docker run --rm -p 8080:8080 tsw-zugdatenberechner
```

Or use Docker Compose:

```
docker compose up --build
```

