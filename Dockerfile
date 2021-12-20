FROM python:3.9.1-buster
RUN apt-get update && apt-get install --no-install-recommends -y default-mysql-client=1.0.5 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN mkdir /servercoins
WORKDIR /servercoins
COPY ./requirements.txt /servercoins
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /servercoins
CMD ["bash", "main_run.sh"]