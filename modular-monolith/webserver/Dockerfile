FROM nginx:alpine

ADD ./dev.conf /etc/nginx/conf.d/default.conf

CMD ["nginx-debug", "-g", "daemon off;"]