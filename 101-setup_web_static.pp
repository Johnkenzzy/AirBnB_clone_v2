# Install Nginx if not already installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create necessary directories
file { [
    '/data',
    '/data/web_static',
    '/data/web_static/releases',
    '/data/web_static/shared',
    '/data/web_static/releases/test',
  ]:
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0755',
  recurse => true,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => '<html>
  <head>
    <title>Test</title>
  </head>
  <body>
    ALX Deployment
  </body>
</html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Create or update the symbolic link
file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  force   => true,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static/releases/test/index.html'],
}

# Ensure ownership of /data/ is recursive to ubuntu user and group
file { '/data':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
  mode    => '0755',
}

# Update the Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx_default.erb'),
  notify  => Service['nginx'],
}

# Restart Nginx to apply changes
exec { 'reload_nginx':
  command     => 'sudo systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
