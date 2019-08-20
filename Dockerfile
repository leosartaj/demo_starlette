FROM python:3.7.4

RUN pip3 install --upgrade pip
RUN pip3 install starlette uvicorn

RUN mkdir /app/

COPY README.md /app/README.md

COPY app.py /app/app.py

WORKDIR /app

CMD ["python3", "app.py"]
