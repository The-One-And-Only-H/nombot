import os
import sys
from slack import WebClient


def main():
    try:
        slack_token = os.environ['NB_SLACK_TOKEN']
    except KeyError:
        print("Please specify the NB_SLACK_TOKEN env var", file=sys.stderr)
        sys.exit(1)

    slack_client = WebClient(slack_token)

    slack_client.chat_postMessage(
        channel="never-cool-ok-bland", text="Happy Friday, folks! Get those noms in: https://goo.gl/forms/mIdOIoBszWmIGHUG3")


if __name__ == '__main__':
    main()
