#!/usr/bin/env python3

##
# Nylas demo with python
#
# Example:
#
#     $ ./nylas-demo-with-python.py
#
# What it does:
#
#   * Nylas connects to your account.
#
#   * Nylas asks for your list of contacts.
#
#   * This demo prints your contacts count.
#     
# ## Nylas setup ##
#
# Set up Nylas as per https://www.nylas.com
#
#
# ## Python setup ##
#
# Install python modules as needed:
#
#     pip3 install nylas
#
#
# ## Environment setup ###
#
# This demo needs these environment variables:
#
#    * NYLAS_DEVELOPER_APP_CLIENT_ID
#
#    * NYLAS_DEVELOPER_APP_CLIENT_SECRET
#
#    * NYLAS_ACCOUNT_ACCESS_TOKEN
#
#
# ## Tracking ##
#
#   * Command: nylas-demo-with-python.py
#   * Version: 1.0.0
#   * Updated: 2019-06-03
#   * License: GPL
#   * Contact: Joel Parker Henderson (joel@contactopensource.com)
#
##

import os
from nylas import APIClient

if "NYLAS_DEVELOPER_APP_CLIENT_ID" not in os.environ:
  sys.exit("Missing NYLAS_DEVELOPER_APP_CLIENT_ID")

if "NYLAS_DEVELOPER_APP_CLIENT_SECRET" not in os.environ:
  sys.exit("Missing NYLAS_DEVELOPER_APP_CLIENT_SECRET")

if "NYLAS_ACCOUNT_ACCESS_TOKEN" not in os.environ:
  sys.exit("Missing NYLAS_ACCOUNT_ACCESS_TOKEN")

nylas = APIClient(
  os.environ['NYLAS_DEVELOPER_APP_CLIENT_ID'],
  os.environ['NYLAS_DEVELOPER_APP_CLIENT_SECRET'],
  os.environ['NYLAS_ACCOUNT_ACCESS_TOKEN']
)

count = nylas.contacts.all().count()

print(f"Nylas contacts count:{count}")
