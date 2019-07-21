#import pytest
from redgreenrefactorcode import RGCMath

class TestRedGreen:
    def test_add(self):
        rgc = RGCMath(4,6)
        #print (rgc)
        #print (rgc.add())
        assert 10 == rgc.add()

def main():
    TestRedGreen().test_add()

main()