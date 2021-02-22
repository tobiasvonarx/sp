from pytube import YouTube


yt = YouTube("https://www.youtube.com/watch?v=NtqqqgDHxD8")

print("downloading: ",yt.title)
stream = yt.streams.filter(only_audio=True).first()
stream.download()