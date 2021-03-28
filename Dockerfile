FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY launch.sh /code/
COPY . /code/

# run entrypoint.sh
ENTRYPOINT ["/code/launch.sh"]
