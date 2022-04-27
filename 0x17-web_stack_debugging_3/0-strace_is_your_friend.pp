# fix phpp extenstion to php
exec { 'fix-wp':
  command  => 'sed -i s/phpp/php/g /var/www/html/wp-setting.php',
  provider => shell,
}