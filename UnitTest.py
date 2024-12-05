import sys
import unittest
from unittest.mock import MagicMock
from services.runner import Runner

class TestRunner(unittest.TestCase):
  def setUp(self):
    self.runner = Runner()
  def test_predict_correct(self):
    self.assertEqual(self.runner.run('hello, it’s me', 'who?'), 'it ’ s me [SEP]')
  def test_predict_incorrect(self):
    self.assertEqual(self.runner.run('xmxsld', 'sdk?'), 'Unable to find the answer to your question.')
  def test_init(self):
    self.assertEqual(self.runner.__init__(), None)
  def test_start(self):
    self.runner.start = MagicMock()
    self.runner.start()
    self.runner.start.assert_called_once()
if __name__ == "__main__":
  unittest.main()
