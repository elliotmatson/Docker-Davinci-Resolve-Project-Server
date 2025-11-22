FROM python:3.14-slim

RUN useradd -m pgadmin-config-creator
RUN mkdir /app && mkdir /config
COPY . /app
RUN chown -R pgadmin-config-creator:pgadmin-config-creator /app /config
USER pgadmin-config-creator

USER pgadmin-config-creator

WORKDIR /app
CMD ["python", "app.py"]
HEALTHCHECK CMD test -f /config/servers.json || exit 1
