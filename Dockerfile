FROM python:3
ADD ekz.py /
ADD test.py /
CMD [ "python", "./test.py" ]
