from plugins.adversary.app.commands.command import CommandLine
from typing import List, Tuple, Callable
from plugins.adversary.app.commands import parsers


def taskkill(args: List[str]=None) -> CommandLine:
    """
    Wrapper for the windows tool taskkill.exe

    Args:
        args: The additional arguments for the command line

    Returns:
        The CommandLine
    """
    command_line = ["taskkill"]

    if args is not None:
        command_line += args

    return CommandLine(command_line)


def by_image(exe_name) -> Tuple[CommandLine, Callable[[str], None]]:
    """
    Taskkill by image name

    Args:
        exe_name: Name of the process to kill, the file name including '.exe' extension
    Returns:
        The CommandLine and a parser for the output of the command
    """
    args = ['/im', exe_name, '/f', '/t']

    return taskkill(args), parsers.taskkill.taskkill


def by_pid(pid: int) -> Tuple[CommandLine, Callable[[str], None]]:
    """
    Taskkill by pid

    Args:
        pid: The pid of the process to kill
    Returns:
        The CommandLine and a parser for the output of the command
    """
    args = ['/pid', str(pid), '/f', '/t']

    return taskkill(args), parsers.taskkill.taskkill
