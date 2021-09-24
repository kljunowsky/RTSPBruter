FROM python:3.9.2-slim-buster

LABEL maintainer="milanjovicsec@sbb.rs"

RUN apt-get update && \
	apt-get install git -y

RUN git clone https://github.com/milan277/RTSPBruter

WORKDIR /RTSPBruter

ENTRYPOINT ["python", "rtspbruter.py"]
