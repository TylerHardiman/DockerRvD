FROM python:3.7.2-alpine

RUN adduser -D FullDadMode
USER FullDadMode
WORKDIR /usr/app

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin${PATH}



LABEL maintainer="Tyler  <Thardiman1989@gmail.com>" \
      version="1.0.0"

CMD [ "python3", "-m" , "run", "--host=0.0.0.0" ]

