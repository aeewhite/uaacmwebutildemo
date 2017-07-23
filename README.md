# uaacmwebutildemo

To try it out:
1. Sign up for a Typeform account.
2. Set up a form, preferably with a first/last name field and email field.
3. Go ahead and be the first person to fill out your form!
4. Grab your API key and form id from Typeform and put them in static.py
5. Run ./setup.sh (may need to run 'chmod u+x setup.sh' first)
6. With the question ids displayed from running the setup (or visible again through running getquestsions.py), put them in the appropriate places in studentdbutil.py
7. Put your email and password in static.py (you may need to modify some security settings on your email account).
8. Run ./startlistener.sh.
9. You're good to go! Try filling out an entry on your Typeform form. It should send emails to respondents and populate a csv file representing your current database.
