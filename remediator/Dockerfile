FROM python:3.12-alpine

# Install Docker CLI to execute container self-healing actions via socket
RUN apk add --no-cache docker-cli

WORKDIR /app
COPY engine.py .

CMD ["python", "-u", "engine.py"]
