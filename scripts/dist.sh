#! /bin/bash

pip install setuptools wheel twine

python ./setup.py sdist
python ./setup.py bdist_wheel
