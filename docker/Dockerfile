FROM debian
ADD debian.list /etc/apt/sources.list.d/
RUN apt-get update && apt-get -y upgrade && apt -y install nginx && apt-get clean && \
    cd /var/www/ && rm -rf ./* && \
    mkdir -p yan.com/img && \
    chmod -R 754 /var/www/yan.com/ && \
    useradd yan && groupadd standart && usermod -aG standart yan && \
    chown -R yan:standart /var/www/yan.com/ && \
    sed -i 's/\/var\/www\/html/\/var\/www\/yan.com/g' /etc/nginx/sites-enabled/default && \
    sed -i 's/user www-data/user yan/g' /etc/nginx/nginx.conf
ADD index.html /var/www/yan.com/
ADD img.jpg /var/www/yan.com/img/
CMD ["nginx", "-g", "daemon off;"]
