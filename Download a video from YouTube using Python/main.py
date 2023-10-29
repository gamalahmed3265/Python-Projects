from pytube import YouTube

# URL of the YouTube video you want to download
video_url = "https://www.youtube.com/shorts/XyzY6o7fxxM"

# Create a YouTube object
yt = YouTube(video_url)

# Select the stream with the desired resolution and file format
# For example, you can choose the highest resolution stream as follows:
video_stream = yt.streams.get_lowest_resolution()

# Set the download location
download_path = "https://www.youtube.com/shorts/XyzY6o7fxxM"

# Download the video
video_stream.download()

print("Video downloaded successfully!")

# Optional: You can also get the video title using yt.title
print("Video Title:", yt.title)
