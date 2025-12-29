class User:
    pass
user1 = User()     # empty class'

def say_hello():
    pass    # empty function
print("hello") # error - indent expeted

# create a class empty
# class User:
#     pass
# # create User object and store in var
# user1 = User()
# user1.name = "Junaid"
# print(user1.name)
#
# # create a user2 object
# user2 = User()
# user2.name = "Alex"
# print(user2.name)

# the above code is too lenthy there is another way:
#-------- ------------------------ Initalize
# # CONSTRUCTOR
# class User:
#     def __init__(self):
#         print("new user being created")
#
# user1 = User()
# user1.name = "Junaid"
# print(user1.name)
#
# user2 = User()
# user2.name = "Alex"
# print(user2.name)

# --------adding attr to class---- Attributes in the constructor -----
# class User:
#     def __init__(self, user_id, user_name):
#         self.id = user_id
#         self.name = user_name
#         self.followers = 0
#
# user1 = User("001", "junaid")
# user2 = User("002", "alex")
#
# print(user1.followers) # default value
# print(user2.name) # given value to object

# --------------------------------
# class names writing rule  -- PascalCase
#-- camelCase
# snake_case


# ------------------------------Adding Methods to class ----------------
# user 1 follows user 2?

class User:
    def __init__(self, user_id , user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0

        # adding methods
    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "junaid")
user2 = User("002", "alex")


user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)