import allure
import pytest
import logging
log = logging.getLogger(__name__)
# 固定写法setup_  module(一个py文件)，function（不在类里面的函数），class（类），method（类里面的方法）
# def setup_module():
#     log.info("模块前置")
#
# def setup_function():
#     log.info("方法前置")
#
# def teardown_function():
#     log.info("方法后置")
#
# def teardown_module():
#     log.info("模块后置")


#fixture默认范围是function
@pytest.fixture(scope="class")
def case_fixture(fixture_one):
    log.info("开始")

    yield

    log.info("结束")

@pytest.fixture(scope="class")
def fixture_one():
    log.info(f"111111")

def test_1(case_fixture):
    assert 1==1

@allure.feature("fixture的使用")
@allure.story("usefixture的使用")
@allure.title("class使用usefixture")
@pytest.mark.usefixtures("case_fixture")
class TestFixtureOne():
    # 给类中的测试用例使用
    def test_2(self):
        assert 2==3

    def test_3(self):
        assert "a" in "abc"


    def test_4(self):
        log.info("22222")



if __name__ == '__main__':
    pytest.main(['-vv','-s'])

