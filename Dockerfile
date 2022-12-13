FROM python:3.10.4
WORKDIR /usr/src
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt && rm requirements.txt
COPY ./api.py .
ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0"]
