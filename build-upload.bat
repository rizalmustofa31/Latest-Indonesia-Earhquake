@echo off
rmdir dist /s /Q
py -m build
py -m twine upload --repository pypi dist/*