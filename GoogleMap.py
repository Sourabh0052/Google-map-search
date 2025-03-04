import webbrowser

firstName = input("Enter first string: ")
lastName = input("Enter second string: ")

result = firstName + " " + lastName  

maps_url = f"https://www.google.com/maps/search/{result}"


webbrowser.open(maps_url)

print("Opening Google Maps with search:", result)
