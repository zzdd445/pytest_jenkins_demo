import sys
import os
from pathlib import Path
import pathlib

# 设置项目根目录到Python路径
project_root = os.path.abspath(os.path.dirname(__file__))
print(project_root)
if project_root not in sys.path:
    sys.path.insert(0, project_root)  # 使用insert(0)确保优先级最高


# 每次执行脚本前清理上次日志，确保日志文件不会过大，实际项目中不会采用
def pytest_configure(config):
    """pytest 收集用例前执行，此时日志文件还没被打开"""
    log_file = pathlib.Path("report/logs/test_run.log")
    if log_file.exists():
        log_file.unlink()
    log_file.parent.mkdir(parents=True, exist_ok=True)