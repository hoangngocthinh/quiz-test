FROM nginx:1.19

RUN rm -f /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/

CMD nginx -g "daemon off;"

# Expose port 80 for web traffic
EXPOSE 80
