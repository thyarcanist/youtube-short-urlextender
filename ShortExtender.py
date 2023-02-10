import webbrowser

# FIFO queue to store URLs
queue = []
queue_size = 10

# Function to open the URL in the web browser
def open_url(url):
    webbrowser.open(url)

while True:
    print('Enter the Youtube Short URL or type "delete cache" to clear the cache:')
    savedURL = input().lower()
    youtubeURL = "https://www.youtube.com/watch?v="

    # Check if user wants to delete the cache
    if savedURL == "delete cache":
        try:
            os.remove("full_urls.txt")
            print("Cache deleted successfully.")
        except:
            print("Cache file not found.")
        continue

    youShortTURL = "https://www.youtube.com/shorts/"
    video_id = savedURL[len(youShortTURL):]
    full_url = youtubeURL + video_id
    isValidURL = True

    if isValidURL:
        print("Converting the URL into a normal URL, would you like to be redirected to the URL? y/n")
        redirectURL = input().lower()

        if redirectURL == 'y':
            open_url(full_url)
            # Add the URL to the FIFO queue
            if len(queue) >= queue_size:
                queue.pop(0)
            queue.append(full_url)
            with open("full_urls.txt", "a") as file:
                file.write(full_url + "\n")
            print("URL added to the cache.")
        elif redirectURL == 'n':
            # Do nothing
            pass
    else:
        print("Invalid URL.")

    # Check if user wants to exit the program
    print("Press q to quit, or any other key to continue.")
    user_input = input().lower()
    if user_input == "q" or user_input == "quit":
        break
