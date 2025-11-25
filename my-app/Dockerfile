FROM python:3.10-slim

WORKDIR /app
RUN pip install flask gunicorn

COPY src/ /app/

EXPOSE 8080
CMD ["python", "app.py"]
