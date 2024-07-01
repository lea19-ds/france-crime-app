FROM ubuntu:latest

RUN mkdir -p /app
RUN apt update && apt-get install -y curl python3 python3-pip file

WORKDIR /app
COPY . .
RUN bash ./install.sh

RUN python3 -m pip install -r requirements.txt

CMD bash launch.sh
