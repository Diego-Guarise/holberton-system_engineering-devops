# login with holberton without errors
exec { 'soft' :
  command  => 'sed -i s/4/4069/ /etc/security/limits.conf',
  provider => shell,
}
exec { 'hard' :
  command  => 'sed -i s/5/4069/ /etc/security/limits.conf',
  provider => shell,
}
