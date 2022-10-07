FROM python:3.9

ENV NOME /app
WORKDIR $NOME

COPY requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt

COPY . .

ENTRYPOINT ["sh", "entrypoint.sh"]