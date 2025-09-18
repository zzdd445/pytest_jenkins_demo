import sys
import os
from pathlib import Path

# 设置项目根目录到Python路径
project_root = os.path.abspath(os.path.dirname(__file__))
print(project_root)
if project_root not in sys.path:
    sys.path.insert(0, project_root)  # 使用insert(0)确保优先级最高