import unittest
class BasicMathTest (unittest.TestCase):
   def runTest (self):
      self.failUnless (2 + 2 == 2 * 2, 'two plus two and two by two not the same!')
      self.failIf (2 + 2 != 2 * 2, 'two plus two and two by two are different')
      self.failUnlessEqual (2 + 2, 2 * 2, 'two plus two and two by two should be equal')
if __name__ == '__main__': 
   unittest.main()
