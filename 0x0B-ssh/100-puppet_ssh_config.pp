# connect to a server Execute a command

file { 'ssh_config':
  path => '/etc/ssh/ssh_config',
  content => 'PasswordAuthentication no\nIdentityFile ~/.ssh/school',
}
