FROM python:3.11-slim

# Evita problemi di buffer nei log
ENV PYTHONUNBUFFERED=1

# Imposta la root del progetto nel PYTHONPATH
ENV PYTHONPATH=/app

# Aggiorna i pacchetti di sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installa le librerie Python
RUN pip install --no-cache-dir numpy requests

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file del tuo progetto
COPY . /app

# Comando di default
CMD ["python3"]
