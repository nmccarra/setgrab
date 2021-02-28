from argparse import ArgumentParser

if __name__ == '__main__':
    parser = ArgumentParser(description="Retrieve setlist from YouTube video")
    parser.add_argument('-url', '--url',
                        default="https://www.youtube.com/watch?v=eFhsH3j4fOU&t=2170s",
                        help="YouTube video URL")
    parser.add_argument('-config_path', '--config_path',
                        default="/main/resources/config.ini",
                        help="path to .ini file with configuration for this application")
    args = parser.parse_args()

    print(args.url)
    print(args.config_path)
