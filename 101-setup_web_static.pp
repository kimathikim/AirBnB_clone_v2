#!/usr/bin/puppet

class web_server_setup {
  package { 'nginx':
    ensure => installed,
  }

  file { '/data/web_static/releases/test/':
    ensure => directory,
  }

  file { '/data/web_static/shared/':
    ensure => directory,
  }

  file { '/data/web_static/releases/test/index.html':
    content => 'Conquistando desde dentro',
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test/',
    require => File['/data/web_static/releases/test/'],
  }

  exec { 'change_ownership':
    command => 'chown -R ubuntu:ubuntu /data/',
    path    => '/usr/bin',
  }

  file { '/etc/nginx/sites-available/default':
    ensure

