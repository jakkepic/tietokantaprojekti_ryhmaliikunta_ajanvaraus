CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
CREATE TABLE instructors (id SERIAL PRIMARY KEY, userid SERIAL REFERENCES users);
CREATE TABLE gymrooms (id SERIAL PRIMARY KEY, roomname Text, capacity INTEGER);
CREATE TABLE classes (id SERIAL PRIMARY KEY, instructorid SERIAL REFERENCES instructors, classname TEXT, sport TEXT, roomid SERIAL REFERENCES gymrooms);
CREATE TABLE bookings (id SERIAL PRIMARY KEY, classid SERIAL REFERENCES classes, userid SERIAL REFERENCES users);