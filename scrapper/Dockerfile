FROM python:3.13-alpine

WORKDIR /app
COPY app .
ENV PYTHONPATH=.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","./main.py"]