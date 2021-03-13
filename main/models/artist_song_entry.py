class ArtistSongTitleEntry:
    """
    class to hold an artist and a related song
    """
    def __init__(self, artist_name, song_title):
        """
        :param artist_name: name of artist
        :param song_title: title of song
        """
        self.artist_name = artist_name
        self.song_title = song_title

    def __str__(self):
        return "ArtistSongTitleEntry({artist_name_str}, {song_title_str})"\
            .format(artist_name_str=self.artist_name, song_title_str=self.song_title)

    def __eq__(self, other):
        return (self.artist_name, self.song_title) == (other.artist_name, other.song_title)
