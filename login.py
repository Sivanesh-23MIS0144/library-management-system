def login(username, password):
    if username == "administrator" and password == "secret":
        return True
    else:
        return False