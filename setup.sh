#!/bin/bash
sudo apt-get install python-pip
sudo -H pip install --upgrade pip
sudo -H pip install typeform
sudo -H pip install sqlalchemy
echo -e "\nQuestion IDs:"
python getquestions.py