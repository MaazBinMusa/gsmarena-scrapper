# Functions for extracting credentials from auth.json to be used in psycopg2

import os
import json
from unicodeconvert import convert

def getAuth():
	# Read the file containing the authentication
	f = open('auth.json', 'r')

	# The file is in json format. Load the contents
	a = json.loads(f.read())

	# Now a contains a dictionary of all auth details but in UTF strings
	# Convert it into normal string
	a = convert(a)

	# return the dictionary. The keys are dbname, user, password and host.
	return a

def getPsqlConnectString():
	# Get the auth dictionary
	credentials = getAuth()

	# Get all credentials
	dbname = credentials.get('dbname')
	user = credentials.get('user')
	password = credentials.get('password')
	host = credentials.get('host')

	# Make a string to be used in psycopg2.connect command
	s = ""
	if dbname:
		s += "dbname=" + dbname
	if user:
		s += " user=" + user
	if password:
		s += " password=" + password
	if host:
		s += " host=" + host

	return s


