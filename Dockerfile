FROM python:3.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./gisdatabase.py ./gisdatabase.py
COPY ./config.py ./config.py
COPY ./main.py ./main.py
COPY ./models/ ./models/
COPY ./controllers/ ./controllers/
COPY ./routers/ ./routers/
COPY ./schemas/ ./schemas/

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8989", "--reload"]

EXPOSE 8989
