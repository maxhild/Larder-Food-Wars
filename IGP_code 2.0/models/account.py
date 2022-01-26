from models.user import User

#Die Klass Account erbt von der Klasse User und wird mit spezifischen Attributen, die nur bei einem Account auftreten erweitert.
#Die Klasse Account wäre kein Muss und die Attribute hätten auch zur Klasse User hinzugefügt werden können, aber es sollte ein möglichst feingranulares
#Klassenkonzept entstehen

class Account(User):

    def __init__(self, firstname, lastname, birthday, user_ID, username, password):
        super(Account, self).__init__(firstname, lastname, birthday)

        self.user_ID = user_ID
        self.username = username
        self.password = password


