# Password Hacker

This project is a password hacking algorithm designed to work with an artificial server. It's a learning project developed on the [Hyperskill](https://hyperskill.org/projects/80) platform.

## Project Description

The algorithm works by attempting to hack the login and password of a server. It uses a combination of brute force and timing attack techniques to guess the correct login credentials. The login names are read from a file named `logins.txt`, and the algorithm tries different combinations of ASCII letters and digits for the password.

The algorithm is implemented in Python and uses the `socket` library to establish a connection with the server. It sends JSON-encoded login credentials to the server and interprets the server's responses to adjust its guessing strategy.

## Usage

To run the password hacker, you need to provide the IP address and port of the server as command-line arguments. Here's an example:

```sh
python script.py 127.0.0.1 9090
```

This will start the password hacking algorithm against the server running at IP address 127.0.0.1 and port 9090.

## Learning Outcomes

This project is a great way to learn about network programming in Python, as well as some basic cybersecurity concepts. It provides hands-on experience with sockets, JSON, and timing attacks.
