class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_credentials(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password
