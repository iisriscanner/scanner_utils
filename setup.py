import setuptools
from pathlib import Path

setuptools.setup(
    name='video_api',
    version='1.0.',
    author='Leo Saif',
    description='Genarate frames from video',
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url='',
    license='MIT',
    packages=['video_api'],
    install_requires=['opencv-python'],
)