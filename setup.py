# Copyright (c) 2021 K.M Ahnaf Zamil

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))
root = path.dirname(here)

readme = path.join(here, 'README.md')
package_json = path.join(here, 'package.json')

with open(readme, "r") as fh:
    long_description = fh.read()

with open(package_json, encoding='utf-8') as f:
    package = json.load(f)

setup(
    name=package['name'],
    author=package['author']['name'],
    author_email=package['author']['email'],
    version=package['version'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=package['homepage'],
    packages=["zenora", "zenora.api", "zenora.impl", "zenora.models"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    exclude=("__pycache__",),
    install_requires=["requests==2.24.0", "attrs==20.3.0"],
)
