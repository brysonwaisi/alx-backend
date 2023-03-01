#!/usr/bin/yarn dev
import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
  console.group('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value);
};

function displaySchoolValue (schoolName) {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
