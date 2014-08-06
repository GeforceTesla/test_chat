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
    parser.add_argument('link',
                        help='The link for chat')
    return parser


def get_latest_chat_loop():
    global latest_count
    global link

    while True:
        time.sleep(1)
        req = requests.get("http://" + link)
        get_count = req.json["count"]
        if get_count > latest_count:
            latest_count = get_count
            read_line = readline.get_line_buffer()
            sys.stdout.write('\r'+' '*(len(readline.get_line_buffer())+2)+'\r')
            sys.stdout.write(str(req.json["id"]) + " says: \n")
            sys.stdout.write(str(req.json["data"]) + "\n")
            sys.stdout.write(read_line)
            sys.stdout.flush()


def post_chat_stuff():
    global identity
    while True:
        inputs = raw_input()
        print "\033[A                             \033[A"
        payload = {"id": identity, "data": str(inputs)}
        req = requests.post("http://" + link, data=payload)

if __name__ == "__main__":
    thread = threading.Thread(target=get_latest_chat_loop)
    thread.daemon = True
    thread.start()

    global identity
    global link
    args = parser().parse_args()
    identity = args.name
    link = args.link
    post_chat_stuff()
