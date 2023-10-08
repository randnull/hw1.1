FROM python:3.10

WORKDIR /game_app/

COPY main.py ./

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "main.py"]