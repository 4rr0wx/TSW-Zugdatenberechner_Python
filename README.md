# TSW Zugdatenberechner

![CI](https://github.com/<owner>/TSW-Zugdatenberechner_Python/actions/workflows/deploy.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)

TSW Zugdatenberechner is a small [Flet](https://flet.dev/) application for calculating train data. The app runs on the desktop and in the browser and is designed to be easy to deploy using Docker and GitHub Actions.

## Features

* Simple user interface built with Flet
* Calculates PZB braking percentage (Brems Hundertstel)
* Animated buttons and dark theme
* Docker support for easy deployment
* GitHub workflow for building and publishing a container image

## Getting started

1. Install the dependencies from `pyproject.toml`:

```bash
poetry install
```

2. Build the app:

```bash
poetry run flet build macos -v
```

3. Run the app locally:

```bash
poetry run flet run
```

## Docker

Build the Docker image and start the container:

```bash
docker build -t tsw-zugdatenberechner .
docker run --rm -p 8080:8080 tsw-zugdatenberechner
```

### Deploy with Docker Compose

A pre-built image is published to the [GitHub Container Registry](https://ghcr.io) as `ghcr.io/OWNER/TSW-Zugdatenberechner_Python:latest` (replace `OWNER` with your GitHub username or organization).

1. Log in to GHCR if required:

   ```bash
   echo "$GITHUB_TOKEN" | docker login ghcr.io -u YOUR_GITHUB_USER --password-stdin
   ```

2. Start the container using the provided Compose file:

   ```bash
   docker compose up -d
   ```

## Deployment

The repository includes a GitHub Actions workflow that builds the Docker image and publishes it to GHCR. Services like [Komodo](https://komodo.dev/) can watch the registry and automatically redeploy the container when a new image is available. The workflow runs on pushes to the `main` branch and requires no additional secrets beyond the default `GITHUB_TOKEN`.

## License

This project is licensed under the terms of the [MIT License](LICENSE).

