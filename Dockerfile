FROM python:3.8-slim

WORKDIR /app

ARG PIP_EXTRA_URL
COPY requirements/app.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --extra-index-url $PIP_EXTRA_URL

COPY . .

CMD ["python", "-m", "run_worker"]