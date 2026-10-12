import qrcode

# Ask for the user's name or message
name = input("Enter your name or a short message: ")

# Generate and save the first QR code
img1 = qrcode.make(name)
img1.save("personal_qrcode.png")

print("Personal QR code saved successfully!")

# Ask for a favorite website
website = input("Enter your favorite website URL: ")

# Generate and save the second QR code
img2 = qrcode.make(website)
img2.save("website_qrcode.png")

print("Website QR code saved successfully!")