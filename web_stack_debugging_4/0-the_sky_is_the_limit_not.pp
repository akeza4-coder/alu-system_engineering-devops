# Increases Nginx open files limit (ULIMIT) in /etc/default/nginx to handle high load

exec { 'fix--for-nginx':
  command => 'sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g" /etc/default/nginx && service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
