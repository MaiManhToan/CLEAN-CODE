# login.py
def login(user, password):
    if user == "admin" and password == "1234":
        return "Login success"
    return "Login failed"
