FROM python:3.10-slim
WORKDIR /app
COPY server.py .
COPY sample.jpeg .
RUN pip install flask
CMD ["python", "server.py"]
