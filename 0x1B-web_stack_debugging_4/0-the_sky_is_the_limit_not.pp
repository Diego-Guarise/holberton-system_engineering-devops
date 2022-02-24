# change limit, acept all
exec { 'change_limit':
  command => 'sed -i s/ULIMIT="-n 15"/ULIMIT="-n 4096"/ /etc/default/nginx',
  path    => '/usr/bin:/bin',
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin'],
  require => Exec['change_limit'],
}
