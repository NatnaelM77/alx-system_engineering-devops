# install nginx and configure it and its header
exec { 'creating custom headers':
  command  => 'name=$(uname -n); sudo apt-get update; sudo apt-get -y install nginx; sudo ufw --force enable; sudo ufw allow "Nginx HTTP"; sudo sed -i -e "s+location / {+location / {\n\t\tadd_header X-Served-By \"$name\";+" /etc/nginx/sites-available/default; sudo service nginx restart;',
  provider => shell,
}