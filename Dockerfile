FROM python:3.6
ADD . /code
WORKDIR /code
EXPOSE 5000
RUN pip install -r requirements.txt
# CMD python madlib.py