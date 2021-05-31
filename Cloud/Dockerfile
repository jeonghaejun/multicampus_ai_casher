FROM python:3.8

RUN pip install Flask
RUN pip install PyMySQL
RUN pip install Requests

COPY /admin_server /admin_server
WORKDIR /admin_server
EXPOSE 5000
CMD ["python","app.py"]