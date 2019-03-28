import sys
sys.path.append('../../pyGenetic/')
import pytest
import Utils
import unittest.mock as mock
import random

@pytest.mark.parametrize("chromosome,expected_results", [
( [0,1], [[1,0]] ),
( [1,2,3], [[1,3,2],[2,1,3]]),
( [1,2,3,4], [[2,1,3,4],[1,3,2,4],[1,2,4,3]] )
])
def test_exhaustive_swap(chromosome,expected_results):
    assert Utils.MutationHandlers.swap(chromosome) in expected_results

@pytest.mark.parametrize("chromosome,random_index, expected_result", [
( [1,2,3], 1, [1,3,2]),
( [1,2,3,4], 1,  [1,3,2,4] ),
( [1,2,3,4,5], 2,  [1,2,4,3,5] )
])
def test_mock_swap(chromosome,random_index,expected_result):
	with mock.patch('random.randint', lambda x,y:random_index):
		assert Utils.MutationHandlers.swap(chromosome) == expected_result


def test_bitFlip():
    pass






if __name__ == '__main__':
    test_swap()
    test_bitFlip()