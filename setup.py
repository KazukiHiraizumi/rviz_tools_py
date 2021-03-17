#!/usr/bin/env python3
# 2021/03/17 hato #!/usr/bin/env python -> !/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=[
        'rviz_tools_py',
    ],
    package_dir={'': 'src'},
)
setup(**d)
