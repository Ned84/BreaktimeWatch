# BreaktimeWatch

[![GitHub license](https://img.shields.io/github/license/Ned84/BreaktimeWatch?color=blue&style=plastic)](https://github.com/Ned84/BreaktimeWatch/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ned84/BreaktimeWatch?style=plastic)](https://github.com/Ned84/BreaktimeWatch/issues)

Program to track breaktimes (coffe- or smokebreak) during workhours. 

* [Description](#description)
* [Dependencies](#dependencies)
* [License](#license)
* [Install](#install)
  * [Build executable from py](#build-executable-from-py)

## Description

Fully editable breaktime tracker.

Times are logged in a JSON file and automatically retrieved uppon start.

Times can be edited via the calendar widget.

![BreaktimeWatch GUI](https://github.com/Ned84/BreaktimeWatch/blob/master/Screenshots/BreaktimeWatch_GUI.png)

## Dependencies

PYQT5 from [this link.](https://pypi.org/project/PyQt5/)

Optional Pyinstaller. Infos are [here.](https://www.pyinstaller.org/downloads.html)

## License 

>Copyright (C) 2019  Ned84 ned84@protonmail.com
>This program is free software: you can redistribute it and/or modify
>it under the terms of the GNU General Public License as published by
>the Free Software Foundation, either version 3 of the License, or
>(at your option) any later version.

>This program is distributed in the hope that it will be useful,
>but WITHOUT ANY WARRANTY; without even the implied warranty of
>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>GNU General Public License for more details.
>You should have received a copy of the GNU General Public License
>along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Install
### Build executable from py
```
pip install pyinstaller
```
```
pyinstaller --onefile --windowed BreaktimeWatch_GUI.py
```



