# Nombot

Python script built for Neverbland sending automated internal weekly nominations form using Slackbot and Crontabs.

Tech stack:

- Python
- Slack client
- Crontabs

The first time you check out the code:

- Create a virtualenv with `virtualenv -p python3 env`
- Install the dependencies using `env/bin/pip install -r requirements.txt`

After which:

- Work in the virtualenv with `source env/bin/activate`
- Export an environment variable with the confidential token: `export NB_SLACK_TOKEN=slack_token`
- Run the script with `python nombot.py`

For the results, run this script instead:

- `python nomresbot.py`

If you want to schedule running the program regularly then you can use this in your crontab:

- `NB_SLACK_TOKEN=<your token>`
- `0 12 * * FRI /Users/h/nom_bot/env/bin/python /Users/h/nom_bot/nombot.py`
- `0 15 * * FRI /Users/h/nom_bot/env/bin/python /Users/h/nom_bot/nombot.py`

- `NB_SLACK_TOKEN=<your token>`
- `0 17 * * FRI /Users/h/nom_bot/env/bin/python /Users/h/nom_bot/nomresbot.py`
