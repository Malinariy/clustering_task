FROM python:3.9.6

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD ["python", "app.py"]
