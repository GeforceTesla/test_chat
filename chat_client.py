import requests
import threading
import time
import sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import readline

latest_count = 0

def parser():
    """Creates a parser that takes in username, password"""
    parser = ArgumentParser(description="Dashboard Flask Server",
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('name',
                        help='The name for chat')
    return parser

def get_latest_chat_loop():
    while True:
        time.sleep(3)
        req = requests.get("http://127.0.0.1:8888/")
        global latest_count
        get_count = req.json["count"]
        if get_count > latest_count:
            latest_count = get_count
            read_line = readline.get_line_buffer()
            sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
            sys.stdout.write( str(req.json["id"]) + " says: \n")
            sys.stdout.write( str(req.json["data"]) + "\n")
            sys.stdout.write(read_line)
            sys.stdout.flush()


def post_chat_stuff():
    global identity
    while True:
        inputs = raw_input()
        print "\033[A                             \033[A"
        payload = {"id": identity, "data": str(inputs)}
        req = requests.post("http://127.0.0.1:8888/", data=payload) 

if __name__ == "__main__":
    thread = threading.Thread(target=get_latest_chat_loop)
    thread.daemon = True
    thread.start()

    global identity
    identity = parser().parse_args().name
    post_chat_stuff()
