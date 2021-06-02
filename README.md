# macOS trash file cleaner
-----
A python program to clean macOS trash files like: ._filename, ._DS_Store, .DS_Store, etc.

## Attention!
These files may be neccessary to macOS system, DO NOT use this program on macOS!

## Usage
Python Version: `3.9.7`
```
python iclean.py
```

## Build for Windows
Install `pyinstaller`: `pip install pyinstaller`
```
pyinstaller -F --icon=pyc.ico iclean.py
```