FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf

RUN apk add openssl

RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
	-keyout /etc/ssl/private/nginx-selfsigned.key \ 
	-out /etc/ssl/certs/nginx-selfsigned.crt \
	-subj '/CN=localhost'

COPY src/static/video /www/static/video

COPY docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY docker/nginx/snippets /etc/nginx/snippets
