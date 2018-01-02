from atx.core import *


t = TestManager(name="Start A New Test For Fun")
ts = t.discover(start='testcases/test_001_a')
for i, item in enumerate(ts):
    print("tc:", i, item)
t.run(ts)

