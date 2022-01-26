#User ist die erste Klasse und die Superklasse von Admin, welche wiederum die Superklasse von Admin und Customer ist.
class User:

    firstname = None
    lastname = None
    birthday = None

    def __init__(self, firstname, lastname, birthday):

        self.firstname = firstname
        self.lastname = lastname
        self.birthday = birthday


