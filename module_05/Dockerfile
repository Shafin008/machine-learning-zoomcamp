# This Dockerfile creates a containerized FastAPI application for serving ML predictions.

# BASE IMAGE
# Use the official Python 3.13.5 slim version based on Debian Bookworm as the base image
# slim means it's stripped down to essentials, keeping the image size small
FROM python:3.13.5-slim-bookworm

# UV Package Manager Integration
# UV is a Rust-based Python package manager that's significantly faster than pip
# This gives you modern dependency management without bloating the image
# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# Multi-stage copy: pulls UV binaries from another image without including that entire image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# WORKING DIRECTORY
# Set the working directory inside the container to /code ((all paths are relative to this))
# All subsequent commands will be run from here
WORKDIR /code

# Environment Configuration
# Add the virtual environment's bin directory to the PATH so Python tools work globally
# Modifies PATH so the virtual environment's executables are accessible globally
# This means you can run python, uvicorn, etc. without prefixing .venv/bin/
ENV PATH="/code/.venv/bin:$PATH"

# Dependency Installation
# Copy the project configuration files into the container
# pyproject.toml     → project metadata and dependencies
# uv.lock            → locked dependency versions (for reproducibility)
# .python-version    → Python version specification
# Layer optimization: copies only dependency files first
# Docker caches layers, so if dependencies don't change, this layer is reused
# Install dependencies exactly as locked in uv.lock, without updating them
# uv sync --locked installs exact versions from uv.lock (ensures reproducibility)
# This happens before copying app code, so code changes don't trigger dependency reinstall
COPY "pyproject.toml" "uv.lock" ".python-version" ./
RUN uv sync --locked

# Application Deployment

# Copy application code and model data into the container
COPY "q3.py" "q4.py" "pipeline_v1.bin" ./
# EXPOSE documents which port the container listens on (metadata for users/orchestrators)
# Expose TCP port 9696 so it can be accessed from outside the container
EXPOSE 9696
# Run the application using uvicorn (ASGI server)
# predict:app → refers to 'app' object inside predict.py
# --host 0.0.0.0 → listen on all interfaces
# --host 0.0.0.0 makes the server accessible from outside the container (not just localhost)
# --port 9696    → listen on port 9696
ENTRYPOINT ["uvicorn", "q4:app", "--host", "0.0.0.0", "--port", "9696"]

# Build it: docker build -t predict-churn .
# then run it: docker run -it --rm -p 9696:9696 predict-churn