# Base image GCC
FROM gcc:12

# Installiamo Python3, pip e strumenti essenziali
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    cmake \
    make \
    gdb \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Creiamo la virtualenv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Aggiorniamo pip e installiamo librerie Python
RUN pip install --upgrade pip
RUN pip install --no-cache-dir requests numpy

# Cartella di lavoro
WORKDIR /workspace

# Comando di default
CMD ["/bin/bash"]
