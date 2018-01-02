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

    def assertTrue(self, expr, msg=""):
        if msg:
            MainLog.info(msg)
        unittest.TestCase.assertTrue(self, expr, msg+" Fail!")

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

    def fetch_tests(self, suite):
        res = []
        if isinstance(suite, TestCase):
            return [suite, ]

        for t in suite:
            if hasattr(t, 'countTestCases'):
                if t.countTestCases:
                    res.extend(self.fetch_tests(t))
            elif t:
                res.append(t)
        return res

    def discover(self, start='testcases', pattern='test_*.py'):
        tcs = unittest.TestSuite()
        if isinstance(start, list) or isinstance(start, tuple):
            for t in start:
                tcs.addTests(self.loader.discover(start_dir=t, pattern=pattern))
        else:
            tcs.addTests(self.loader.discover(start_dir=start, pattern=pattern))
        return self.fetch_tests(tcs)

    def run(self, tests=()):
        for i in tests:
            self.testsuite.addTest(i)

        MainLog.info("Atx - Auto Test Ex Version {}.{}".format(self.VERSION_MAJOR, self.VERSION_MINOR))

        MainLog.info("=============================================")
        MainLog.info("============== auto test start ==============")
        MainLog.info("=============================================")
        self.result = self.runner.run(self.testsuite)
        MainLog.info("=============================================")
        MainLog.info("=============== auto test end ===============")
        MainLog.info("=============================================")
        return self.result




