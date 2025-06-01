# -----------------------------------------------------------------------------
# dockerfile
#
# Builds the FastAPI application container.
#
# Steps:
#   - Uses Python 3.10 base image.
#   - Sets working directory to /app.
#   - Copies application code and requirements.
#   - Installs dependencies from requirements.txt.
#   - Runs the FastAPI app with Uvicorn on port 8000.
# -----------------------------------------------------------------------------
FROM python:3.10

WORKDIR /app
COPY ./rest_api /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY lint.sh .
RUN chmod +x lint.sh && ./lint.sh


CMD ["uvicorn", "rest_api.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
