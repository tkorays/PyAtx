import unittest
import logging
import logging.config
import os


class TestCase(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)


class TestManager:
    def __init__(self, name="test", start_dir='testcases', pattern='test_*.py', top_level_dir='.'):
        self.name = name
        self.loader = unittest.TestLoader()
        self.test_cases = self.loader.discover(start_dir=start_dir, pattern=pattern, top_level_dir=top_level_dir)
        self.runner = unittest.TextTestRunner(verbosity=2)

        logging.config.fileConfig(os.path.join('.', 'config/logging.ini'))

    def run(self):
        logging.info("===============================")
        logging.info("======= auto test start =======")
        logging.info("===============================")
        self.runner.run(self.test_cases)
        logging.info("===============================")
        logging.info("======== auto test end ========")
        logging.info("===============================")

