import ytdownloader

print("Videos oder Playlists?")
eingabe1 = input()
if eingabe1.lower().startswith("play"):
    print("Gib die URL ein")
    url = input()
    print("Metadaten und Phumbnail herunterladen?")
    eingabe2 = input()
    metadata = "false"
    if eingabe2.lower().startswith("j"):
        ytdownloader.metadata_play(url)
    ytdownloader.playlist(url)
if eingabe1.lower().startswith("vid"):
    video_list = []
    print("Gib URL(s) ein (end to end)")
    while True:
        url = input("")
        if url.lower().startswith("stop") or url.lower().startswith("end"):
            break
        video_list.append(url)
    print("Metadaten herunterladen?")
    eingabe3 = input()
    metadata = "false"
    if eingabe3.lower().startswith("j"):
        ytdownloader.metadata_vids(video_list)
    ytdownloader.videos(video_list)
