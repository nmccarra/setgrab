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

    @staticmethod
    def parse_to_artist_song_entry(acr_raw_object):
        """
        parse an ACR response object to ArtistSongTitleEntry instances
        :param acr_raw_object: response from ACR Content Recognition API as an object
        :return: list of ArtistSongTitleEntry or None if status.msg is not 'Success'
        """
        if acr_raw_object.status.msg == "Success":
            output = [ArtistSongTitleEntry(artist_name=e.artists[0].name, song_title=e.title) for e in
                      acr_raw_object.metadata.music]
        else:
            output = None
        return output

    def prune_results(self, d, keys_left):
        """
        tail recursive function which prunes a dict of recurrent consecutive values
        :param d: dict
        :param keys_left: keys from d left to iterate over
        :return: pruned dict
        """
        if len(keys_left) == 1:
            return d
        else:
            if d[keys_left[0]] == d[keys_left[1]]:
                d.pop(keys_left[1])
                keys_left.pop(1)
                return self.prune_results(d, keys_left)
            else:
                keys_left.pop(0)
                return self.prune_results(d, keys_left)

    def parse(self, acr_results_dict):
        """
        parsing function which returns a dict that has been pruned of entries identified by an earlier
        consecutive (key, value) and with values that are only the most frequent artist/song identified
        :param acr_results_dict: dict object with keys that are instances of HourMinutesSecondsMark
        and values which are the raw object of the response from the ACR Cloud API
        :return: pruned dict with keys that are HourMinutesSecondsMark and values which are ArtistSongTitleEntry
        """
        dict_w_song_entry_values = {k: self.parse_to_artist_song_entry(v) for (k, v) in acr_results_dict.items()}
        dict_w_single_most_frequent_entry = {k: max(v, key=lambda item: (item.artist_name, item.song_title)) for (k, v) in dict_w_song_entry_values.items() if
                                             v is not None}

        key_list = list(dict_w_single_most_frequent_entry.keys())
        sorted_key_list = sorted(key_list, key=lambda x: (x.hour, x.minutes, x.seconds))
        return self.prune_results(dict_w_single_most_frequent_entry, sorted_key_list)
