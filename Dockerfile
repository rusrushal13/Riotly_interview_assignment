FROM python:3.6-alpine
LABEL Rushal Verma<rusrushal13@gmail.com>
COPY . /app
WORKDIR /app
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials.json
CMD pip install --upgrade -r requirements.txt && python riotly-etl.py