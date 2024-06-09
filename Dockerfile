FROM python:3.11-slim
LABEL maintainer="xerxez.in"

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /gen_ai

# Copy the requirements file
COPY requirements.txt .

# Install system dependencies and Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-venv && \
    python3 -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    useradd --no-log-init --system --create-home webapp

# Copy the application code
COPY . .
COPY navigation.py navigation.py
#COPY .env .env

# Set environment variables for the virtual environment
ENV PATH="/py/bin:$PATH"

# Expose the application port
EXPOSE 8501

# Change to non-root user
USER webapp

# Debugging steps to verify everything is in place
RUN echo "Checking Python version:" && python --version
RUN echo "Checking pip version:" && pip --version
RUN echo "Listing installed packages:" && pip list
RUN echo "Listing files in working directory:" && ls -la /gen_ai

# Set entrypoint and default command
ENTRYPOINT ["streamlit", "run"]
CMD ["streamlit_app.py"]
