user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Write your code here!
# Class declaration
class User:
    def __init__(self, user_id="", level=0):
        self.user_id = user_id
        self.level = level

# Create the first User object using initial values.
user1 = User("codetree", 10)

# Declare variables and input
user2_level = int(user2_level)

# Create the second User object using provided input values.
user2 = User(user2_id, user2_level)

# Output
print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")