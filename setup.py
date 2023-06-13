import setuptools
from pathlib import Path

NAME = "scanner_utils"

setuptools.setup(
    name=NAME,
    version="1.2.1",
    author="Leo Saif",
    description="Genarate frames from video",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/iisriscanner/{NAME}",
    license="MIT",
    packages=[f"{NAME}"],
    install_requires=["opencv-python", "Pillow"],
)
