# Everything in the nxapi is an object, similar to pynautobot

# DME - Data Management Engine - handles requests/responses
# MIT - Management Information Tree - similar to YANG data model, 
# structures data so the DME knows how/where to get data

# Each object has 2 names:
# 	1. Relative name - file.txt
# 	2. Distinguished name - /home/user/docs/file.txt (DNs are unique)


import requests

user = 'admin'
password = 'Admin_1234!'