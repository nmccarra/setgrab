from main.models.artist_song_entry import ArtistSongTitleEntry


class ACRResultsParser:
    """
    A class for parsing the JSON responses from ACRCloudClient method instances
    which call out to the ACR Cloud Content Recognition API
    """
    def __init__(self, config):
        """
        :param config: full config file in main/resources/config.ini
        """
        self.config = config

    def parse_to_artist_song_entry(self, acr_raw_object):
        """
        parse an ACR response object to ArtistSongTitleEntry instances
        :param acr_raw_object: response from ACR Content Recognition API as an object
        :return: list of ArtistSongTitleEntry or None if status.msg is not 'Success'
        """
        if acr_raw_object.status.msg == "Success":
            output = [ArtistSongTitleEntry(artist_name=e.artists[0].name, song_title=e.title) for e in acr_raw_object.metadata.music]
        else:
            output = None
        return output
