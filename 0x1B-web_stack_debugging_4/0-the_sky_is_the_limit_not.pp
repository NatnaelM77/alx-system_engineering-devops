# fix too many open files
exec { 'fix-nginx':
  command  => 'sed -i -e "s/15/4096/" /etc/default/nginx; service nginx restart',
  provider => shell,
}
