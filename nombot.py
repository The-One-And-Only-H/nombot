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
        channel="neverbland", text="Happy Friday, folks! Get those noms in: https://goo.gl/forms/mIdOIoBszWmIGHUG3")

if __name__ == '__main__':
    main()

# Replace form with interactive bot so users can submit noms directly via the bot for example:
# User: Hey nombot, I'd like to submit a nom
# Bot: Sure thing, pal! Please submit your nom with the following format: Name: *enter name here* Nom: *enter nom here* For example: Name: H Nom: H is the best
# User: Name: H Nom: H is the best
# Bot: Thanks for submitting your nom, buddy! *gif*
