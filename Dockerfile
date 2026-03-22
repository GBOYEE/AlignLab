# Dockerfile for AlignLab
FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir -r requirements-dev.txt

# Copy source
COPY src ./src
COPY tests ./tests
COPY data ./data
COPY docs ./docs

CMD ["pytest", "--cov=src", "tests/"]