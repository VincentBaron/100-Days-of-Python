class User:
    def __init__(self, id, username):
        print("new user being created...")
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("#1", "Vinny")
user_2 = User("#2", "Victor")
user_1.follow(user_2)

print(f"user_1.id = {user_1.id}")
print(f"user_1.username = {user_1.username}")
print(f"user_1.following = {user_1.following}")
print(f"user_1.followers = {user_1.followers}\n\n")
print(f"user_2.id = {user_2.id}")
print(f"user_2.username = {user_2.username}")
print(f"user_2.following = {user_2.following}")
print(f"user_2.followers = {user_2.followers}")

