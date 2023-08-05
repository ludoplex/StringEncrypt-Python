#!/usr/bin/env python

###############################################################################
#
# StringEncrypt WebApi interface usage example.
#
# In this example we will verify our activation code status.
#
# Version        : v1.0
# Language       : Python
# Author         : Bartosz Wójcik
# Project page   : https://www.stringencrypt.com
# Web page       : https://www.pelock.com
#
###############################################################################

#
# include StringEncrypt module
#
from stringencrypt import StringEncrypt

#
# if you don't want to use Python module, you can import it directly from the file
#
#from stringencrypt.stringencrypt import StringEncrypt

#
# create StringEncrypt class instance (we are using our activation code)
#
myStringEncrypt = StringEncrypt("ABCD-ABCD-ABCD-ABCD")

if result := myStringEncrypt.is_demo():
	print(f'Demo version status - {"True" if result["demo"] else "False"}')

	print(f'Label length limit - {result["label_limit"]}')
	print(f'String length limit - {result["string_limit"]}')

	print(f'File bytes limit - {result["bytes_limit"]}')

	print(f'Usage credits left - {result["credits_left"]}')
	print(f'Total usage credits - {result["credits_total"]}')

	print(f'Min. number of encryption commands - {result["cmd_min"]}')
	print(f'Max. number of encryption commands - {result["cmd_max"]}')

else:
	print("Something unexpected happen while trying to login to the service.")
