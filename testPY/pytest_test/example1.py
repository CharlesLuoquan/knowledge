# fixture函数的作用域仅限于此测试文件
import pytest


@pytest.fixture()
def fixtureFunc():
    return 'fixtureFunc666'


def test_fixture(fixtureFunc):
    print('我调用了{}'.format(fixtureFunc))


