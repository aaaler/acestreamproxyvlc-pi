FROM resin/rpi-raspbian:jessie
RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  unzip ca-certificates
RUN adduser --disabled-password --gecos "" tv
RUN cd / && wget http://aler.me/~aler/acestream-rpi-3.1.14.0.tgz -O acestream-rpi-3.1.14.0.tgz && tar xvzf acestream-rpi-3.1.14.0.tgz && rm -f acestream-rpi-3.1.14.0.tgz
EXPOSE 62062
ENTRYPOINT ["/acestream/start_acestream.sh"]
