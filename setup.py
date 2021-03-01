#!/usr/bin/env python

import setuptools

long_description="""python-evt is a pure Python parser for classic Windows Event Log files (".evt")."""

setuptools.setup(name="python-evt",
      version="0.1",
      description="Pure Python parser for classic Windows event log files (.evt).",
      long_description=long_description,
      author="Willi Ballenthin",
      author_email="willi.ballenthin@gmail.com",
      url="https://github.com/williballenthin/python-evt",
      license="Apache 2.0 License",
      packages=setuptools.find_packages())
