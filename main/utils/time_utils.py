def time_mm_ss_to_seconds(s):
    """
    converts string in the form mm:ss e.g. "22:59" to seconds
    """
    minutes_seconds_split = s.split(":")
    return int(minutes_seconds_split[0]) * 60 + int(minutes_seconds_split[1])
