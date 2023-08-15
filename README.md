# SpartanLog
A minimal application to allow team members to log into and out of the lab during meetings.

## Running
Python requirements can be installed with `pip install -r requirements.txt`.

Flask expects a `SESSION_SECRET` environment variable to be set to some random private key. Unix-like systems can do this quickly with `SESSION_SECRET="$(xxd -l 16 -p /dev/random)"`.

Specify the application entry point with `FLASK_APP=main.py`, and run it locally with `flask run`.

## List of things to do:
- Alignment on the nav-bar
- Add database
- Add list formatting
