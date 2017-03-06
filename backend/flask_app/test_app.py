from app import *
import unittest
from mock import Mock

class AppTestCase(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True;

	def test_get_data(self):
		result = self.app.get('/exam/api/v1.0/data') 