FROM p0bailey/docker-flask

COPY requirements.txt server.py /server/

RUN pip install -r /server/requirements.txt

COPY  flask_app /server/flask_app/

WORKDIR /server

EXPOSE 5000

CMD ["python", "manage.py", "init_data_and_run_server"]

