# install nginx and configure it
exec { 'creating custom headers':
  command  => 'apt-get update apt-get -y install nginx ufw allow 'Nginx HTTP' sed -i '/index index.html index.htm index.nginx-debian.html/a \\tadd_header X-Served-By '$HOSTNAME';\n \terror_page 404 /404.html;\n \trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default service nginx reload',
  provider => shell,

