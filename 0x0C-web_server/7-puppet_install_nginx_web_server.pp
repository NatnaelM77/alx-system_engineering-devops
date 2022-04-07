#Install nginx web server
package { 'nginx':
  ensure => installed,
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.google.com  permanent;',
}

file { '/var/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure => running,
  package => Package['nginx'],
}
