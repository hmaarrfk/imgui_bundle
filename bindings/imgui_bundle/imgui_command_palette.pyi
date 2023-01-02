"""a Sublime Text or VSCode style command palette in ImGui
https://github.com/hnOsmium0001/imgui-command-palette
"""
from typing import List
import enum
from imgui_bundle.imgui import ImFont, ImU32
ImGuiCond = int


class Context:
    pass


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:imcmd_command_palette.h>    ####################


# TODO support std::string_view
# TODO support function pointer callback in addition to std::function

class ImCmdTextType(enum.Enum):
    regular = enum.auto()   # (= 0)
    highlight = enum.auto() # (= 1)
    count = enum.auto()     # (= 2)

""" namespace ImCmd"""
class Command:
    name: str
    initial_callback: std.function<None()>
    subsequent_callback: std.function<None(int selected_option)>
    terminating_callback: std.function<None()>
    def __init__(self) -> None:
        """Autogenerated default constructor"""
        pass


#/ Destroys the currently bound context.


# Command management
def add_command(command: Command) -> None:
    pass
def remove_command(name: str) -> None:
    pass

# Styling
def set_style_font(type: ImCmdTextType, font: ImFont) -> None:
    pass
def set_style_color(type: ImCmdTextType, color: ImU32) -> None:
    pass
def clear_style_color(type: ImCmdTextType) -> None:
    """< Clear the style color for the given type, defaulting to ImGuiCol_Text"""
    pass

# Command palette widget
def set_next_command_palette_search(text: str) -> None:
    pass
def set_next_command_palette_search_box_focused() -> None:
    pass
def command_palette(name: str) -> None:
    pass
def is_any_item_selected() -> bool:
    pass

def remove_cache(name: str) -> None:
    pass
def remove_all_caches() -> None:
    pass

# Command palette widget in a window helper
def set_next_window_affixed_top(cond: ImGuiCond = 0) -> None:
    pass
def command_palette_window(name: str, p_open: bool) -> bool:
    pass

def prompt(options: List[str]) -> None:
    """ Command responses, only call these in command callbacks (except TerminatingCallback)"""
    pass


####################    </generated_from:imcmd_command_palette.h>    ####################


####################    <generated_from:imgui-command-palette-py-wrapper.h>    ####################


# Workaround for ImCmd::Context, since pybind11 stubbornly fails on perfect encapsulation
# ImCmd::Context is perfectly encapsulated, since it is only defined privately in a C++ file, and not in a header.
# See https://github.com/pybind/pybind11/issues/2770

class ContextWrapper:
    def __init__(self) -> None:
        pass

####################    </generated_from:imgui-command-palette-py-wrapper.h>    ####################

# </litgen_stub> // Autogenerated code end!
