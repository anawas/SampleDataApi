
class AllowedUsers:
    def __init__(self):
        self.users = [
            "bernerj",
            "bessererm",
            "erned",
            "gulerj",
            "kellers",
            "marquesj",
            "melligerm",
            "michels",
            "rajicf",
            "roses",
            "schenkelm",
            "schmids",
            "werrenj",
            "zizzas",
        ]

    def is_allowed_user(self, user, password):
        if user in self.users and password == 'abbts-sya':
            return True
        return False
