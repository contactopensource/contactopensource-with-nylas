#!/usr/bin/env ruby

##
# Nylas demo with ruby
#
# Example:
#
#     $ ./nylas-demo-with-ruby.rb
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
# ## Ruby setup ##
#
# Install ruby gems as needed:
#
#     gem install nylas
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
#   * Command: nylas-demo-with-ruby.py
#   * Version: 1.0.0
#   * Updated: 2019-06-03
#   * License: GPL
#   * Contact: Joel Parker Henderson (joel@contactopensource.com)
#
###


require 'nylas'

ENV['NYLAS_DEVELOPER_APP_CLIENT_ID'] or abort('Missing NYLAS_DEVELOPER_APP_CLIENT_ID')
ENV['NYLAS_DEVELOPER_APP_CLIENT_SECRET'] or abort('Missing NYLAS_DEVELOPER_APP_CLIENT_SECRET')
ENV['NYLAS_ACCOUNT_ACCESS_TOKEN'] or abort('Missing NYLAS_ACCOUNT_ACCESS_TOKEN')

nylas = Nylas::API.new(
  app_id: ENV['NYLAS_DEVELOPER_APP_CLIENT_ID'],
  app_secret: ENV['NYLAS_DEVELOPER_APP_CLIENT_SECRET'],
  access_token: ENV['NYLAS_ACCOUNT_ACCESS_TOKEN']
)

count = nylas.contacts.count

p "Nylas contacts count:#{count}"
