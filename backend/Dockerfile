# Dockerfile

FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
# RUN pip3 install gunicorn

# CMD ["gunicorn", "-b", ":5001", "app:app"]
CMD ["python3", "-m", "app", "run", "--host=0.0.0.0"]
