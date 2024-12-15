
FROM python:3.12-slim

COPY  backend.py .

RUN pip install flask

EXPOSE 5000
CMD ["python", "backend.py"]
