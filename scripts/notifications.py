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
