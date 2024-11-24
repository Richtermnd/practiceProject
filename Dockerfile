FROM python:3.13

WORKDIR app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src .

CMD ["python", "main.py"]