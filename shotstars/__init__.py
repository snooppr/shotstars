import sys
import os

# путь к папке (__init__.py и папке plotext)
package_dir = os.path.dirname(os.path.abspath(__file__))

# локальный plotext "перекрывает" системный
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

from .shotstars import main_cli
