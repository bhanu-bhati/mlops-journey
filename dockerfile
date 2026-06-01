# 1. Start with a lightweight, clean Linux image that has Python pre-installed
FROM python:3.10-slim

# 2. Set the working directory inside the container's virtual hard drive
WORKDIR /app

# 3. Copy our server file from your Mac into the container's /app folder
COPY server.py .

# 4. Install the precise libraries needed to run the backend engine
RUN pip install fastapi uvicorn

# 5. Open up port 8000 so web traffic can reach our API container
EXPOSE 8000

# 6. The exact command to fire up our live server when the container boots
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

