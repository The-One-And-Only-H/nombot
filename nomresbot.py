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
        channel="U50GU82V9", text="Nom results here: https://docs.google.com/spreadsheets/d/1KTJ1Fmu3RxfgpPdivSJ8AizfrYe80P7GiosKaRFFrvo/edit#gid=340226277")

    slack_client.chat_postMessage(
        channel="UKP6THU7Q", text="Nom results here: https://docs.google.com/spreadsheets/d/1KTJ1Fmu3RxfgpPdivSJ8AizfrYe80P7GiosKaRFFrvo/edit#gid=340226277")

    slack_client.chat_postMessage(
        channel="U029WUVCG", text="Nom results here: https://docs.google.com/spreadsheets/d/1KTJ1Fmu3RxfgpPdivSJ8AizfrYe80P7GiosKaRFFrvo/edit#gid=340226277")

    slack_client.chat_postMessage(
        channel="UFJN8LZJN", text="Nom results here: https://docs.google.com/spreadsheets/d/1KTJ1Fmu3RxfgpPdivSJ8AizfrYe80P7GiosKaRFFrvo/edit#gid=340226277")


if __name__ == '__main__':
    main()

# Leah: U50GU82V9
# Faraday: UKP6THU7Q
# Scott: U029WUVCG
# H: UFJN8LZJN
