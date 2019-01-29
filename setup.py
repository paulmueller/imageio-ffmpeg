"""
Setup script for imageio-ffmpeg.
"""

import os
import sys

from setuptools import setup

this_dir = os.path.dirname(os.path.abspath(__file__))

# Get version
sys.path.insert(0, os.path.join(this_dir, "imageio_ffmpeg"))
try:
    from _definitions import __version__
finally:
    sys.path.pop(0)


# Disallow releasing via setup.py
if "upload" in sys.argv:
    raise RuntimeError("Running setup.py upload is not the proper release procedure!")


# If making a source dist, clear the binaries directory
if "sdist" in sys.argv:
    target_dir = os.path.abspath(os.path.join(this_dir, "imageio_ffmpeg", "binaries"))
    for fname in os.listdir(target_dir):
        if fname != "README.md":
            os.remove(os.path.join(target_dir, fname))


long_description = """
FFMPEG functionality for imageio.

Note that the platform-specific wheels contain the binary executables
of ffmpeg and ffprobe, which makes this package a bit over 100 MiB in size.
I guess that's the cost for being able to read/write video files.

For Linux users: the above is not the case when installing via your
Linux package manager (if that is possible), because this package would
simply depend on ffmpeg anf ffprobe in that case.
""".lstrip()


setup(
    name="imageio-ffmpeg",
    version=__version__,
    author="imageio contributors",
    author_email="almar.klein@gmail.com",
    license="(new) BSD",
    url="https://github.com/imageio/imageio-ffmpeg",
    download_url="http://pypi.python.org/pypi/imageio-ffmpeg",
    keywords="video ffmpeg",
    description="FFMPEG functionality for imageio",
    long_description=long_description,
    platforms="any",
    provides=["imageio_ffmpeg"],
    python_requires=">=3.4",
    install_requires=[],  # todo: maybe numpy
    packages=["imageio_ffmpeg"],
    package_dir={"imageio_ffmpeg": "imageio_ffmpeg"},
    package_data={"imageio_ffmpeg": ["binaries/*.*"]},
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)