Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.9
* virtualenv + pip
* Git

eg, on Ubuntu:

	sudo add-apt-repository ppa:deadsnakes/ppa
	sudo apt update
	sudo apt install nginx git python3.9 python3.9-venv
	
## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., boleypickem.club

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., boleypickem.club

