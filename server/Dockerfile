FROM python:3.10-slim
WORKDIR /app
COPY server.py .
COPY sample.jpg .
RUN pip install flask opencv-python-headless
CMD ["python", "server.py"]
