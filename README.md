# Ansible playbook to setup Engelsystem 

This is a role to install the Engelsystem. You can use it to install directly or to include it in your own ansible playbooks.

## Prerequisites

You will need a server running Debian 10 with SSH key auth.

## Usage

First of all, clone this repository and cd into the newly created directory.

Configure:

* Rename the inventory file `inventory/example` to `server` and replace the servername in it.
* Rename the configuration file `inventory/host_vars/server.example.com.yml` to match the servername in your inventory file.
* Edit the configuration file to your needs.

Run:

```sh
# Method 1
# 
# Connect as your_user and sudo with the password ansible asks you
ansible-playbook -u your_user -b -K -i inventory/server site.yml

# Method 2
#
# Connect as root
ansible-playbook -u root -i inventory/server site.yml
```

## Install Ansible

If you have trouble installing ansible on your system you can try this:

```sh
python -m venv env
. env/bin/activate
pip install ansible
```

When you open a new shell you have to reenable the virtualenv:

```sh
. env/bin/activate
```

More info on venv is in the Python docs: https://docs.python.org/3/library/venv.html
