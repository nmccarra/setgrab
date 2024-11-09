import unittest
from configparser import ConfigParser
from uuid import uuid4

from main.services.segment_generator import SegmentGenerator
import os
from shutil import copyfile
from shutil import rmtree

hash_folder_name = uuid4().hex


class TestSegmentGenerator(unittest.TestCase):

    def setUp(self):
        if os.getcwd().endswith("test"):
            self.dir = os.getcwd()
            self.dir_prefix = ""
        else:
            self.dir = os.getcwd() + "/test"
            self.dir_prefix = "test/"

        self.config = ConfigParser()
        self.config.read(self.dir.removesuffix("test") + "/resources/test/config.ini")
        self.segment_generator = SegmentGenerator(config=self.config, hash_folder_name=hash_folder_name)
        if not os.path.exists(self.dir + "/.tmp"):
            os.mkdir(self.dir + "/.tmp")
        os.mkdir(self.dir + "/.tmp/" + hash_folder_name)
        copyfile(self.dir.removesuffix("test") + "/resources/test/download.mp3",
                 self.dir + "/.tmp/" + hash_folder_name + "/download.mp3")

    def tearDown(self):
        rmtree(self.dir + "/.tmp")

    def test_should_generate_segments(self):
        segment_dict = self.segment_generator.segment(0, 10 * 60, prefix=self.dir_prefix)
        self.assertEqual(4, len(segment_dict.keys()))
        return 0
