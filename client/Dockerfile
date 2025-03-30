FROM python:3.10-slim
WORKDIR /app
COPY client.py .
RUN pip install flask requests
CMD ["python", "client.py"]
