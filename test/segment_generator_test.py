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
        self.config = ConfigParser()
        self.config.read(os.getcwd()+"/resources/config.ini")
        self.segment_generator = SegmentGenerator(config=self.config, hash_folder_name=hash_folder_name)
        if not os.path.exists(os.getcwd() + "/.tmp"):
            os.mkdir(os.getcwd() + "/.tmp")
        os.mkdir(os.getcwd() + "/.tmp/" + hash_folder_name)
        copyfile(os.getcwd() + "/resources/download.mp3", os.getcwd() + "/.tmp/" + hash_folder_name + "/download.mp3")

    def tearDown(self):
       rmtree(os.getcwd() + "/.tmp/" + hash_folder_name)

    def test_should_generate_segments(self):
        segment_dict = self.segment_generator.segment()
        self.assertEqual(4, len(segment_dict.keys()))
        return 0
