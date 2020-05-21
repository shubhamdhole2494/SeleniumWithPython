import os

import pytest

@pytest.fixture()
def setUp():
    print("Set up method is executed")

def test_MethodA(setUp):
    print("Running method A")


def test_MethodB(setUp):
    print("Running method B")

def getCurrentWorkingDirectory(setUp):
    currDir = os.getcwd()
    print(currDir)
