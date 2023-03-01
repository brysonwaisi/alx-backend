#!/usr/bin/yarn dev
import { createClient } from "redis";

const client = createClient();
client.on('error', (err) => {
  console.group('Redis client not connected to the server: ERROR_MESSAGE');
});

client.on('connect', () => {
  console.log('Redis client connected to the server')
})
