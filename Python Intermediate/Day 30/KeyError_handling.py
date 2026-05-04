facebook_posts = [
    {"Likes": 1, "Comments": 1},
    {"Likes": 2, "Comments": 2, "Shares":5},
    {"Likes": 5, "Comments": 4, "Shares":6},
    {"Comments": 3, "Shares:":4},
    {"Comments": 4, "Shares:":2},
    {"Likes": 2, "Comments": 2}
]


total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes += 0 # or use pass

print(total_likes)