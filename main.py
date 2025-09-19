import pytest
import os

def main():
    # 运行测试并生成报告
    pytest.main()
    os.system("allure generate ./report/allure_raw -o ./report/allure_html --clean")

if __name__ == "__main__":
    main()