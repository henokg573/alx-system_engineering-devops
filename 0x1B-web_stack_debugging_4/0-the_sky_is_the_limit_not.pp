# increase the ULIMIT of the default file
# Fixing the number of failed requests to get to 0
exec { 'fix--for-nginx':
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
# Restart nginx
exec { 'nginx start':
    # Restart the nginx service
    command => '/etc/init.d/nginx restart',
    # specify the path for the init.d script
    path => '/etc/init.d',
}
