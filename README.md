# BreaktimeWatch

[![GitHub license](https://img.shields.io/github/license/Ned84/BreaktimeWatch?color=blue&style=plastic)](https://github.com/Ned84/BreaktimeWatch/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ned84/BreaktimeWatch?style=plastic)](https://github.com/Ned84/BreaktimeWatch/issues)
[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2F%2FNed84%2FBreaktimeWatch%2Fbadge&style=plastic)](https://actions-badge.atrox.dev//Ned84/BreaktimeWatch/goto)
[![CircleCI](https://circleci.com/gh/Ned84/BreaktimeWatch.svg?style=svg)](https://circleci.com/gh/Ned84/BreaktimeWatch)

Program to track breaktimes (coffe- or smokebreak) during workhours. 

* [Description](#description)
  * [BreaktimeWatch](#breaktimewatch)
  * [WorktimeWatch](#worktimewatch)
* [Dependencies](#dependencies)
* [License](#license)
* [Install](#install)
  * [Build executable from .py](#build-executable-from-py)
* [Support](#support)
* [Get my Public Key](#get-my-public-key)

## Description

### BreaktimeWatch

Editable breaktime tracker.

Times are logged in a JSON file and automatically retrieved uppon start.

Times can be edited via the calendar widget.

### WorktimeWatch

Editable workhour tracker.

Workhours are logged and the average working time for the current workweek to achieve the minimum workhours per week is calculated.


![BreaktimeWatch GUI](https://github.com/Ned84/BreaktimeWatch/blob/master/Screenshots/BreaktimeWatch_GUI.png)

![BreaktimeWatch GUI](https://github.com/Ned84/BreaktimeWatch/blob/master/Screenshots/BreaktimeWatch_GUI_2.png)

## Dependencies

 Newest Python from [here.](https://www.python.org/downloads/)

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
### Build executable from .py
```
pip install pyinstaller
```
```
pip install PyQt5
```
```
pyinstaller --windowed --icon=Icon/btwbgr_white_FIz_3.ico --clean --name BreaktimeWatch.py BreaktimeWatch_GUI.py
```

## Support

If you require help or if you have suggestions please refer to the [Issue section](https://github.com/Ned84/BreaktimeWatch/issues).

## Get my Public Key

Get my public key at [Keybase](https://keybase.io/ned84).


