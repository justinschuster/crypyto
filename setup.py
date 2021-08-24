import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
    name="crypyto-pkg-justinschuster",
    version="0.0.1",
    author="Justin Schuster",
    author_email="schujustin@gmail.com",
    description="Desktop cryptocurrency tracking application",
    python_requires=">=3.6"
)