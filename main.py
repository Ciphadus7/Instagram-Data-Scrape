import instaloader
#create an instance of instaloader
bot = instaloader.Instaloader()

print("Please log into your Instagram ID:")
# Interactive login on terminal
yourID = input("Please enter your Instagram ID - ")
bot.interactive_login(yourID) # Asks for password in the terminal

while True:
    #query the person to load a profile from an instagram handle
    queryA = input('Please enter an Instagram handle - ')
    queryB = input('Would you like to view the queried profile\'s information or download it\'s post(s)?[View = V. Download = D] - ')


    if queryB == 'V':
        profile = instaloader.Profile.from_username(bot.context, queryA)
        print(type(profile))
        #print more info
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers: ", profile.followers)
        print("Followees: ", profile.followees)
        print("Bio: ", profile.biography,profile.external_url)


    if queryB == 'D':
        profile = instaloader.Profile.from_username(bot.context, queryA)
        # Get all posts in a generator object
        posts = profile.get_posts()

        # Iterate and download
        for index, post in enumerate(posts, 1):
            bot.download_post(post, target=f"{profile.username}_{index}")


    continuation = input('Would you like to re-run the script or exit?(r = re-run. e = exit)? - ')

    if continuation == 'r':
        continue
    elif continuation == 'e':
        break