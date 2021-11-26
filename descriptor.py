from pytube import YouTube, Playlist

class Descriptor:
  playlist_url = ""

  def __init__(self, playlist_url):
    self.playlist_url = playlist_url

  def bytes_to_MB(self, bytes):
    return bytes / (1024 ** 2)

  def video_download_size(self, video_url):
    yt = YouTube(video_url)

    stream = yt.streams.filter(file_extension="mp4", res="360p").first()
    return stream.filesize_approx

  def get_playlist_download_size(self, playlist_url):
    p = Playlist(playlist_url)
    
    download_size = 0
    for i in range(len(p.videos)):
      download_size += self.video_download_size(p.video_urls[i])
    
    return self.bytes_to_MB(download_size)
    
  def describe(self):
    return "Download Size:  " + str(int(self.get_playlist_download_size(self.playlist_url))) + "MB"
