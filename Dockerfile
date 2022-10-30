# ./Dockerfile
FROM python:3.10
WORKDIR /usr/src/app

#Set enviroment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk update
#RUN apk add postgresql-dev gcc python-3dev musl-dev zlib-dev jpeg-dev

## Copy all src files
COPY . .

## Install packages
#RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Run the application on the port 8080
EXPOSE 8000

# gunicorn 배포 명령어
# CMD ["gunicorn", "--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stock.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0:8000"]