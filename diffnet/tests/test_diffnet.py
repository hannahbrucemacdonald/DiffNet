"""
Unit and regression test for the diffnet package.
"""

# Import package, test suite, and other packages as needed
import diffnet
import pytest
import sys

def test_diffnet_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "diffnet" in sys.modules
