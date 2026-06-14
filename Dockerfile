FROM nginx:alpine
RUN apk add --no-cache apache2-utils
COPY html/ /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx/.htpasswd_user /etc/nginx/.htpasswd_user
COPY nginx/.htpasswd_admin /etc/nginx/.htpasswd_admin
EXPOSE 80