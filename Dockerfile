FROM python:2.7
RUN pip install --upgrade pip
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python app.py
