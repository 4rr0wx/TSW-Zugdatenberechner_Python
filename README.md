# Flet app

Flet app using Flet extension.

This version allows entering custom wagons to calculate the PZB train type
based on the brake ratio. Each vehicle can be added with its mass, brake weight
and length directly in the UI.

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

In the app enter the vehicle data for each wagon and click **Hinzufügen**. When
all wagons are listed press **Berechnen** to see the total mass, brake weight
and PZB category.

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

## Command line calculator

To calculate train data from a custom configuration on the command line run:

```
python -m src.train_calculator_cli
```

The script will ask for the vehicle data of each wagon or locomotive and
outputs the resulting train mass, brake weight, brake ratio and PZB type.

