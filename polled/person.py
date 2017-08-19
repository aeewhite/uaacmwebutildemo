class Person(object):
    firstName = ''
    lastName = ''
    email = ''
    slack = ''
    size = ''
    def __init__(self, firstName, lastName, email, slack, size):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.slack = slack
        self.size = size