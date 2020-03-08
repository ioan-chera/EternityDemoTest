"""
    Test Demos Python Script: regression test of DOOM demos in Eternity
    Copyright (C) 2020  Ioan Chera

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import platform
import subprocess

IS_MACOS = platform.system() == 'Darwin'

if not IS_MACOS:
    from pynotifier import Notification


def _applescript_escaped(text):
    """
    Necessary for passing a string into an AppleScript text, to prevent injection.
    :param text: The text to escape
    :return: The escaped text
    """
    return text.replace('"', '\\"')


def show(text):
    """
    Shows a notification on a temporary popup to the user
    :param text: The text to show
    :return: nothing
    """
    if IS_MACOS:
        subprocess.call(['osascript', '-e',
                         f'display notification "{_applescript_escaped(text)}" with title "Eternity demo test"'])
    else:
        Notification(title='Eternity demo test', description=text).send()
