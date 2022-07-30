FROM python:3.8-alpine
RUN mkdir -p /{app,config}
COPY . /app
WORKDIR /app
CMD ["python", "app.py"]
HEALTHCHECK CMD test -f /config/servers.json || exit 1