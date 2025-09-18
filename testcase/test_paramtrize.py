import allure
import pytest
from conftest import project_root
from utils.read_data import read_yaml

file_path = str(project_root)+"/data/data.yaml"
list_data = read_yaml(file_path)


@allure.feature("数据驱动")
@allure.story("多参数+单参数")
class TestParamtrize():

    # 单参数循环，@pytest.mark.parametrize("key",['value'])
    # 运行时将数组里面的数据多次赋值给变量，每赋值一次运行一次，用例条数取决于数据,
    @allure.title("单参数")
    @pytest.mark.parametrize("name",['明世隐',"后羿","小乔","王昭君"])
    def test_a(self,name):
        print(f"我是{name}")
        assert isinstance(1,int)
        assert name == "明世隐"


    # 多参数循环
    @allure.title("多参数")
    @pytest.mark.parametrize("name,word",[("明世隐","巴拉巴拉"),("小乔","嘟嘟嘟嘟"),("瑶","云梦泽")])
    def test_b(self,name,word):
        print(f"我是{name},{word}")


    # 多参数,前面的参数是key，例如："case_name,num1,num2,sum"，后面的是可迭代的数据list_data
    @allure.title("从外部读取yaml文件多参数")
    @pytest.mark.parametrize("case_name,num1,num2,sum",list_data)
    def test_c(self,case_name,num1,num2,sum):
        print(f"我是测试用例{case_name}")
        assert num1+num2 == sum



