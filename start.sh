#!/usr/bin/env bash
########################################
# Start script for Husky test project. #
########################################

# Let's start with updating packages list!
apt-get update

# Python 3 is already installed by default in Ubuntu 14.04 But pip isn't.
# Let's change it!
apt-get install -y python3-pip

# Now we need to install required packages. From definition of test project
# we assume that our project will be used in Docker container, so we actually
# don't need to isolate our project.
#
# Therefore we can actually install Django system-wide
pip3 install Django==1.8.5

# Applying migrations
python3 manage.py migrate

# Run server
#
# Note: I can't test it by myself, since my router doesn't work well with VMs.
# Tho tests with port forwarding says that everything is alright.
python3 manage.py runserver 0.0.0.0:80
