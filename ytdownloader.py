import pytube
import urllib.request


def playlist(url_playlist):
    pl = pytube.Playlist(url_playlist)
    for vid in pl:  # Go through every video in the playlist and passing it to the video downloader
        video(vid)
        return str(vid).title()


def video(url_video):
    yt = pytube.YouTube(url_video)
    print("Downloading: " + yt.title)
    yt.streams.filter(progressive=True).get_highest_resolution().download(output_path="YT")  # Download the video in the
    # highest resolution which has also audio in it (720p/30)
    print("Done with " + yt.title)
    # data(url_video)  # Passing the video to the data class to download other "metadata"


def videos(urls):
    for vids in enumerate(urls):  # Go through every video and passing it to the video downloader
        video(str(vids))


def thumbnail(url):
    yt = pytube.YouTube(url)
    print(yt.thumbnail_url)
    urllib.request.urlretrieve(yt.thumbnail_url, "YT/" + yt.title + "_thumbnail.jpg")  # Download the thumbnail


def metadata_vids(urls):
    for vids in enumerate(urls):  # Go through every video and downloading the data
        metadata(urls)


def metadata_play(url):
    pl = pytube.Playlist(url)
    for vid in pl:  # Go through every video in the playlist and downloading the data
        metadata(url)


def metadata(url):
    data(url)
    thumbnail(url)


def data(url):
    yt = pytube.YouTube(url)
    print("Downloading Data for " + yt.title)
    metadata = "URL: " + url + "\nTitel: " + str(yt.title) + "\nAuthor: " + str(yt.author) + "\nAufrufe: " \
               + str(yt.views) + "\nRating: " + str(yt.rating) + "\nTags: " + str(yt.keywords) \
               + "\n--------------------\n" + str(yt.description)
    file = open("YT/" + yt.title + "_data.txt", "w")  # Make a file in the YT folder which is called the title_data.txt
    file.write(metadata)  # Write the data from data to the file
    file.close()
    print("Downloading Done for " + yt.title)