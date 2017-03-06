import unittest
from mock import Mock
from dataMidlayer import *
from ..dao.dataEsDao import *

class TestDataMidlayer(unittest.TestCase):

	def setUp(self):
		self.mockDao = DataEsDao
		self.mockDao.search = Mock(return_value=MockResult())
		self.midlayer = DataMidlayer(self.mockDao)

	def test_get_data(self):
		expected = [ 'test' ]
		sample_query = {
			'test': 1,
			'test': 2
		}
		res = self.midlayer.get_data(sample_query)
		self.mockDao.search.assert_called_with(sample_query)
		self.assertEqual(res, expected)

class MockResult:

	def to_dict(self):
		return {
			'hits': {
				'hits' : [
					{ '_source' : 'test' }
				]
			}
		}
