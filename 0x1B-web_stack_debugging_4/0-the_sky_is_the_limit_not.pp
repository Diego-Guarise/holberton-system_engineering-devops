# change limit, acept all
exec { 'change_limit':
  command => 'sed -i s/15/4069/ /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
