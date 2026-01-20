FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy seluruh source code
COPY . .

# (Opsional) pastikan encoding & buffering aman
ENV PYTHONUNBUFFERED=1

# Jalankan aplikasi
CMD ["python", "main.py"]