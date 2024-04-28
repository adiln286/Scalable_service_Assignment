class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
