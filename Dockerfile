# ---- Base image ----
FROM python:3.11-slim

# ---- Environment variables ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# ---- Set work directory ----
WORKDIR /app

# ---- Install system dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy requirements first (for layer caching) ----
COPY requirements.txt .

# ---- Install Python dependencies ----
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---- Copy project files ----
COPY . .

# ---- Expose Streamlit port ----
EXPOSE 8501

# ---- Run Streamlit app ----
CMD ["streamlit", "run", "app.py"]
