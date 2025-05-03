FROM python:3.11-slim  # Matches your Python 3.11 requirement

# Install system libraries (if needed for audio/opus)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]  # Same as your Replit entrypoint