FROM python:3.12-slim

RUN apt-get update
RUN apt-get install -y build-essential
RUN pip install --upgrade pip


WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

CMD [ "python3", "app.py" ]