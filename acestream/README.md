dockerized Acestream for raspberry pi 2/3 arm armhf


Example:

`docker run --privileged --rm --name acestream -p 62062:62062 aaaler/acestream-pi --client-console --live-buffer 50 --max-connections 400 --max-peers 200`
