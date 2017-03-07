FROM p0bailey/docker-flask

COPY requirements.txt manage.py /server/

RUN pip install -r /server/requirements.txt

COPY  flask_app /server/flask_app/

WORKDIR /server

EXPOSE 5000

RUN python manage.py init_data

CMD ["python", "manage.py", "run_server"]

