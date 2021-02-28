from argparse import ArgumentParser
from configparser import ConfigParser


if __name__ == '__main__':
    parser = ArgumentParser(description="Retrieve setlist from YouTube video")
    parser.add_argument('-url', '--url',
                        default="https://www.youtube.com/watch?v=eFhsH3j4fOU&t=2170s",
                        help="YouTube video URL")
    parser.add_argument('-config_path', '--config_path',
                        default="./main/resources/config.ini",
                        help="path to .ini file with configuration for this application")
    args = parser.parse_args()

    config = ConfigParser()
    config.read(args.config_path)
    acr_config = config['acr-cloud']

    print(args.url)
    print(args.config_path)
    print(dict(acr_config))

