FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Install system dependencies for OpenCV and other libraries
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Verify templates directory exists and list contents
RUN ls -la /app/ && \
    ls -la /app/templates/ || echo "Templates directory not found!" && \
    ls -la /app/static/ || echo "Static directory not found!"

# Create necessary directories
RUN mkdir -p uploads static/results json_results

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=7860

EXPOSE 7860

CMD ["python", "app.py"]