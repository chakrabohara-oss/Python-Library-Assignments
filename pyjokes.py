import pyjokes

# Display three jokes
for i in range(3):
    joke = pyjokes.get_joke()
    print(f"\nJoke {i + 1}: {joke}")

# Ask the user if they want another joke
while True:
    answer = input("\nDo you want another joke? (yes/no): ").lower()

    if answer == "yes":
        print("\n", pyjokes.get_joke())
    elif answer == "no":
        print("Thank you for using the joke generator!")
        break
    else:
        print("Please enter yes or no.")
