#!/bin/bash
virtualenv .env 
if [ -d .env/bin ]
then
	source .env/bin/activate 
else
	exit -1
fi
pip install -r requirements.txt
