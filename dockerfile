FROM python:3.10-slim
WORKDIR /app

# Copy configuration files and our trained brain into the image
COPY requirements.txt .
COPY server.py .
COPY house_model.pkl .

# Install everything listed in our requirements file
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]

