import emoji

# Ask for the user's name
name = input("Enter your name: ")

# Display a welcome message
print(emoji.emojize(f"Hello {name}! :smile:"))

# Ask for the favorite activity
activity = input("What is your favorite activity? ")

# Display a personalized greeting
print(emoji.emojize(f"Enjoy {activity}! :thumbs_up:"))
print(emoji.emojize("Keep learning Python! :red_heart:"))
