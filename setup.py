from distutils.core import setup

setup(
    name="adventofcode",
    version="0.1",
    packages=[],
    license="MIT",
    entry_points={
        'console_scripts': [
            'aocdriver = aoc.core.driver:main'
        ]
    }
)
