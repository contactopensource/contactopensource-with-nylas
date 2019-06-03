#!/usr/bin/env node

////
// Nylas demo with node
//
// Example:
//
//     $ node --experimental-modules nylas-demo-with-node.js
//
// What it does:
//
//   * Nylas connects to your account.
//
//   * Nylas asks for your list of contacts.
//
//   * This demo prints your contacts count.
//     
// ## Nylas setup ##
//
// Set up Nylas as per https://www.nylas.com
//
//
// ## Node setup ##
//
// Install node packages as needed:
//
//     npm install nylas
//
//
// ## Environment setup ###
//
// This demo needs these environment variables:
//
//    * NYLAS_DEVELOPER_APP_CLIENT_ID
//
//    * NYLAS_DEVELOPER_APP_CLIENT_SECRET
//
//    * NYLAS_ACCOUNT_ACCESS_TOKEN
//
////

import Nylas from 'nylas';

if (!('NYLAS_DEVELOPER_APP_CLIENT_ID' in process.env)) {
  console.error("Missing NYLAS_DEVELOPER_APP_CLIENT_ID");
  process.exit(1);
}

if (!('NYLAS_DEVELOPER_APP_CLIENT_SECRET' in process.env)) {
  console.error("Missing NYLAS_DEVELOPER_APP_CLIENT_SECRET");
  process.exit(1);
}

if (!('NYLAS_ACCOUNT_ACCESS_TOKEN' in process.env)) {
  console.error("Missing NYLAS_ACCOUNT_ACCESS_TOKEN");
  process.exit(1);
}

Nylas.config({
  appId: process.env.NYLAS_DEVELOPER_APP_CLIENT_ID,
  appSecret: process.env.NYLAS_DEVELOPER_APP_CLIENT_SECRET
});
 
var nylas = Nylas.with(process.env.NYLAS_ACCOUNT_ACCESS_TOKEN);
 
nylas
  .contacts
  .count()
  .then(
    count => {
      console.log(`You have ${count} contacts.`);
    }
  );
