# 此文件的fixture被多个测试文件共享
import pytest


@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc66612345'


def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))


