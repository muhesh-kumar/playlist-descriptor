from pytube import YouTube, Playlist

def bytes_to_MB(bytes):
  return bytes / (1024 ** 2)

def video_download_size(video_url):
  yt = YouTube(video_url)

  stream = yt.streams.filter(file_extension="mp4", res="360p").first()
  return stream.filesize_approx

def playlist_download_size(playlist_url):
  p = Playlist(playlist_url)
  print(p.title)
  
  download_size = 0
  for i in range(len(p.videos)):
    download_size += video_download_size(p.video_urls[i])
  
  return bytes_to_MB(download_size)
  
playlist_url = input("Enter the URL of the playlist: ")
print("Extension: mp4")
print("Resolution: 360p")
print("Download Size:  " + str(int(playlist_download_size(playlist_url))) + "MB")