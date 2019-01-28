# -*- coding: utf-8 -*-

import os
import unittest
import configparser

from ankisyncd.persistence import PersistenceManager
from ankisyncd.persistence import get_persistence_manager

import helpers.server_utils

class FakePersistenceManager(PersistenceManager):
    def __init__(self, config):
        pass

class BadPersistenceManager:
    pass

class PersistenceManagerFactoryTest(unittest.TestCase):
    def test_get_persistence_manager(self):
        # Get absolute path to development ini file.
        script_dir = os.path.dirname(os.path.realpath(__file__))
        ini_file_path = os.path.join(script_dir,
                                     "assets",
                                     "test.conf")

        # Create temporary files and dirs the server will use.
        server_paths = helpers.server_utils.create_server_paths()

        config = configparser.ConfigParser()
        config.read(ini_file_path)

        # Use custom files and dirs in settings. Should be PersistenceManager
        config['sync_app'].update(server_paths)
        self.assertTrue(type(get_persistence_manager(config['sync_app']) == PersistenceManager))

        # A conf-specified PersistenceManager is loaded
        config.set("sync_app", "persistence_manager", 'test_persistence.FakePersistenceManager')
        self.assertTrue(type(get_persistence_manager(config['sync_app'])) == FakePersistenceManager)

        # Should fail at load time if the class doesn't inherit from  SimplePersistenceManager
        config.set("sync_app", "persistence_manager", 'test_persistence.BadPersistenceManager')
        with self.assertRaises(TypeError):
            pm = get_persistence_manager(config['sync_app'])



