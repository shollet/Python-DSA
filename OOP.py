# class StarCookie:
#     milk = 0.1

#     def __init__(self, color, weight):
#         self.color = color
#         self.weight = weight


# starCookie1 = StarCookie("red", 15)
# StarCookie.milk = 0.2
# print(starCookie1.color, starCookie1.weight, starCookie1.__dict__)
# starCookie2 = StarCookie("blue", 16)
# print(starCookie2.color, starCookie2.weight, starCookie2.__dict__)
# print(StarCookie.__dict__)
# print(starCookie1.milk)
# print(starCookie2.milk)

class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions
    
    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = Youtube("Elshad")
user2 = Youtube("Renad")
user1.subscribe(user2)
print(user1.username, user1.subscribers, user1.subscriptions)
print(user2.username, user2.subscribers, user2.subscriptions)