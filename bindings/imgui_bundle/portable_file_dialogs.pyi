"""Portable GUI dialogs library, C++11, single-header
https://github.com/samhocevar/portable-file-dialogs
"""

# ruff: noqa: B008
import enum

from typing import List

# Process wait timeout, in milliseconds
default_wait_timeout = 20

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:portable_file_dialogs_simplified.h>    ####################

class button(enum.Enum):
    cancel = enum.auto()  # (= -1)
    ok = enum.auto()  # (= 0)
    yes = enum.auto()  # (= 1)
    no = enum.auto()  # (= 2)
    abort = enum.auto()  # (= 3)
    retry = enum.auto()  # (= 4)
    ignore = enum.auto()  # (= 5)

class choice(enum.Enum):
    ok = enum.auto()  # (= 0)
    ok_cancel = enum.auto()  # (= 1)
    yes_no = enum.auto()  # (= 2)
    yes_no_cancel = enum.auto()  # (= 3)
    retry_cancel = enum.auto()  # (= 4)
    abort_retry_ignore = enum.auto()  # (= 5)

class icon(enum.Enum):
    info = enum.auto()  # (= 0)
    warning = enum.auto()  # (= 1)
    error = enum.auto()  # (= 2)
    question = enum.auto()  # (= 3)

class opt(enum.Enum):
    """Additional option flags for various dialog constructors"""

    none = enum.auto()  # (= 0)
    # For file open, allow multiselect.
    multiselect = enum.auto()  # (= 0x1)
    # For file save, force overwrite and disable the confirmation dialog.
    force_overwrite = enum.auto()  # (= 0x2)
    # For folder select, force path to be the provided argument instead
    # of the last opened directory, which is the Microsoft-recommended,
    # user-friendly behaviour.
    force_path = enum.auto()  # (= 0x4)

class notify:
    """
    The notify widget

    """

    def __init__(self, title: str, message: str, _icon: icon = icon.info) -> None:
        pass

    def ready(self, timeout: int = default_wait_timeout) -> bool:
        pass

    def kill(self) -> bool:
        pass

class message:
    """
    The message widget

    """

    def __init__(
        self,
        title: str,
        text: str,
        _choice: choice = choice.ok_cancel,
        _icon: icon = icon.info,
    ) -> None:
        pass

    def result(self) -> button:
        pass

    def ready(self, timeout: int = default_wait_timeout) -> bool:
        pass

    def kill(self) -> bool:
        pass

def all_files_filter() -> List[str]:
    pass

class open_file:
    """
    The open_file, save_file, and open_folder widgets

    """

    def __init__(
        self,
        title: str,
        default_path: str = "",
        filters: List[str] = all_files_filter(),
        options: opt = opt.none,
    ) -> None:
        pass

    def ready(self, timeout: int = default_wait_timeout) -> bool:
        pass

    def kill(self) -> bool:
        pass

    def result(self) -> List[str]:
        pass

class save_file:
    def __init__(
        self,
        title: str,
        default_path: str = "",
        filters: List[str] = all_files_filter(),
        options: opt = opt.none,
    ) -> None:
        pass

    def ready(self, timeout: int = default_wait_timeout) -> bool:
        pass

    def kill(self) -> bool:
        pass

    def result(self) -> str:
        pass

class select_folder:
    def __init__(
        self, title: str, default_path: str = "", options: opt = opt.none
    ) -> None:
        pass

    def ready(self, timeout: int = default_wait_timeout) -> bool:
        pass

    def kill(self) -> bool:
        pass

    def result(self) -> str:
        pass

####################    </generated_from:portable_file_dialogs_simplified.h>    ####################

# </litgen_stub> // Autogenerated code end!
