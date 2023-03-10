FROM python:3.7
RUN pip install --upgrade pip
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python3 app.py
