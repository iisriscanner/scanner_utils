import setuptools
from pathlib import Path

setuptools.setup(
    name='scanner_api',
    version='1.1.0',
    author='Leo Saif',
    description='Genarate frames from video',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url='https://github.com/iisriscanner/scanner_utils',
    license='MIT',
    packages=['scanner_utils'],
    install_requires=['opencv-python'],
)