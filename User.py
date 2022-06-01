# your User class goes here

import random


PEOPLE_NAMES = ["Sky", "Jack", "Casper", "Mike", "Raph"]
PEOPLE_MAILS = ["sky@email.com", "Jack@email.com", "Casper@email.com", "Mike@email.com", "Raph@email.com"]

class User():
    # We create a class that uses simple params to emulate a registration -> now allows for posting content!

    all_user_posts = []

    def __init__(self, user_name, user_email_address):
        self.name = user_name
        self.email_address = user_email_address
        self.my_posts = []
    
    def __str__(self):
        return f"NAME: {self.name}, EM: {self.email_address}, Posts: {self.my_posts}"

    

    def addPost(self, content):
        self.my_posts.append({'name': self.name, 'content' : content})
        User.all_user_posts.append({'name': self.name, 'content' : content})

    def removePost(self):
        for i in reversed(range(len(self.my_posts))):
            if self.my_posts[i]['name'] == self.name:
                print("FOUND", self.my_posts[i]['name'], self.my_posts[i]['content'])
                del self.my_posts[i]
                break;
        for j in reversed(range(len(User.all_user_posts))):
            if User.all_user_posts[j]['name'] == self.name:
                print("FOUND", User.all_user_posts[j]['name'], User.all_user_posts[j]['content'])
                del User.all_user_posts[j]
                break;

sky = User("sky", "sky@skymail.com")
jt = User("jt", "jt@jtmail.com")
print(sky)
sky.addPost("TEST")
jt.addPost("TEST_2")
sky.addPost("TEST_3")
# print(sky)
# print(User.all_user_posts)
sky.removePost()
print(sky)
print(User.all_user_posts)