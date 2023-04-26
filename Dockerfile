FROM python:3.9.12

ADD converter.py /
CMD [ "python3", "./converter.py" ]