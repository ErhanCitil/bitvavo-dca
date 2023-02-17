Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess bitvavo_dca-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/bitvavo_dca/log/apache2/error.log"
        CustomLog "/srv/sites/bitvavo_dca/log/apache2/access.log" common

        WSGIProcessGroup bitvavo_dca-<target>

        Alias /media "/srv/sites/bitvavo_dca/media/"
        Alias /static "/srv/sites/bitvavo_dca/static/"

        WSGIScriptAlias / "/srv/sites/bitvavo_dca/src/bitvavo_dca/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-bitvavo_dca-<target>]
    user = <user>
    command = /srv/sites/bitvavo_dca/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/bitvavo_dca/src/bitvavo_dca/wsgi/wsgi_<target>.py
    home = /srv/sites/bitvavo_dca/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/bitvavo_dca/log/uwsgi_err.log
    stdout_logfile = /srv/sites/bitvavo_dca/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_bitvavo_dca_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/bitvavo_dca/log/nginx-access.log;
      error_log /srv/sites/bitvavo_dca/log/nginx-error.log;

      location /500.html {
        root /srv/sites/bitvavo_dca/src/bitvavo_dca/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/bitvavo_dca/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/bitvavo_dca/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_bitvavo_dca_<target>;
      }
    }
