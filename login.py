def login(username, password):
    if username == "superuser" and password == "secret":
        return True
    else:
        return False