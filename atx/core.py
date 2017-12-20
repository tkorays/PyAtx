import logging.config as logging_config
import os
import sys
import unittest
import ddt
import logging
from atx.config import AtxConfig

DdtDecorator = ddt.ddt
DdtData = ddt.data
MainLog = logging
MsgLog = logging.getLogger('message')


class TestCase(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName=methodName)

    def run(self, result=None):
        MainLog.info('')
        MainLog.info('~'*45)
        MainLog.info('TestCase Name   : {}.{}'.format(self.__class__.__name__, self._testMethodName))
        MainLog.info('TestCase Module : {}'.format(self.__module__))
        MainLog.info('~'*45)
        super().run(result)
        MainLog.info('Test Done!')


class TestRunner(unittest.TextTestRunner):
    def run(self, test):
        pass


class TestManager:
    VERSION_MAJOR = 1
    VERSION_MINOR = 0

    def __init__(self, name="test"):
        self.name = name
        self.loader = unittest.TestLoader()
        self.testsuite = unittest.TestSuite()
        self.result = None
        self.runner = unittest.TextTestRunner(verbosity=2, stream=sys.stderr)
        self.config = AtxConfig('config/atx.ini')

        logging_config.fileConfig(os.path.join('.', self.config.get_log_config()))

    def run(self, start='testcases', pattern='test_*.py'):
        if isinstance(start, list) or isinstance(start, tuple):
            for t in start:
                self.testsuite.addTests(self.loader.discover(start_dir=t, pattern=pattern))
        else:
            self.testsuite.addTests(self.loader.discover(start_dir=start, pattern=pattern))

        MainLog.info("Atx - Auto Test Ex Version {}.{}".format(self.VERSION_MAJOR, self.VERSION_MINOR))

        MainLog.info("=============================================")
        MainLog.info("============== auto test start ==============")
        MainLog.info("=============================================")
        self.result = self.runner.run(self.testsuite)
        MainLog.info("=============================================")
        MainLog.info("=============== auto test end ===============")
        MainLog.info("=============================================")
        return self.result




