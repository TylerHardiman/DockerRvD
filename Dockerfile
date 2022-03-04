FROM python:3
RUN pip install pystrich

WORKDIR /RVD ./

# here we create a new user
# note how the commands are using &&
# this helps with caching


COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}

# 👇 here we set the user

CMD [ "python3", "redis-server" ]