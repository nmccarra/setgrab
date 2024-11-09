class ParsedResultsFormatter:
    """
    A class which takes the parsed JSON from the results parser
    and formats it for presentation to user
    """

    def __init__(self, config):
        self.config = config

    @staticmethod
    def format(parsed_results_dict):
        """
        :param parsed_results_dict: a dict with keys that are HourMinutesSecondsMark and values that are ArtistSongTitleEntry
        :return: list of dict entries containing the time, artist and track of the setlist item
        """
        output = []
        for (k, v) in parsed_results_dict.items():
            output.append(
                {
                    "time": k.as_youtube_time_mark(),
                    "artist": v.artist_name,
                    "track": v.song_title
                }
            )

        return output

    @staticmethod
    def format_as_text(parsed_results_dict):
        """
        :param parsed_results_dict: a dict with keys that are HourMinutesSecondsMark and values that are ArtistSongTitleEntry
        :return: string block containing the time mark and the song recognised at the mark
        """
        sorted_time_marks = sorted(list(parsed_results_dict.keys()), key=lambda x: (x.hour, x.minutes, x.seconds))
        result = ""
        for time_mark in sorted_time_marks:
            artist_song_title_entry = parsed_results_dict[time_mark]
            result = result + time_mark.as_youtube_time_mark() + " ~ " + artist_song_title_entry.artist_name + " - " + artist_song_title_entry.song_title + "\n"
        return result
