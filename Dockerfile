FROM python:3.6

WORKDIR /app
ADD . .
RUN python setup.py install

ENTRYPOINT [ "python", "app.py" ]