# register.py
users = []

def register(username, password):
    users.append({"username": username, "password": password})
    print(f"User {username} registered successfully!")

if __name__ == "__main__":
    register("alice", "abc123")
    register("bob", "xyz789")
