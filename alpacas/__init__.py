# Define shortcut to function
from alpacas.common.game_enums import myfunc
from alpacas.other.otherfunc import printme

# When doing an import *, only import these functions
__all__ = ['myfunc', 'printme']
