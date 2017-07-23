# uaacmwebutildemo

To try it out:
1. Sign up for a Typeform account.
2. Set up a form, preferably with a first/last name field and email field.
3. Grab your API key and form id from Typeform and put them in static.py
3. Run ./setup.sh
4. With the question ids displayed from running the setup (or visible again through running getquestsions.py), put them in the appropriate places in studentdbutil.py
5. Put your email and password in static.py (you may need to modify some security settings on your email account).
6. Run ./startlistener.sh.
7. You're good to go! Try filling out an entry on your Typeform form. It should send emails to respondents and populate a csv file representing your current database.