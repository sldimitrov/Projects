import pafy

# opening the text file which contains all the links
file = open('list.txt', 'r')

# loop through each link in the file
for line in file:

    # Assign link to "url" variable
    url = line

    try:
        # Passing link to pafy
        video = pafy.new(url)

        # extracting the best available audio
        bestaudio = video.getbestaudio()
        print(video.title)

        # downloading the extracted audio
        bestaudio.download()

    # move to next link if the video is removed in the youtube platform
    except:
        pass

# close the text file
file.close()
