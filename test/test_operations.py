import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from pytest import fixture
from travistest_ import Operations

@fixture
def op():
	
	return Operations.Operations()

def test_add(op):
	assert op.add(1,2) == 3

def test_subtract(op):
	assert op.subtract(2,1) ==1

def test_increment(op):
	assert op.increment(2)==3

def test_decrement(op):
	assert op.decrement(3)==2