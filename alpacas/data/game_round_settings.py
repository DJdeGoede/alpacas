#! /usr/bin/env python3
'''
the __init__.py file in the alpacas top level package dir
can be used to define imports in advance so you can then use them
in the import statements in underlaying modules.

The __all__ list at the end in the alpacas/__init__.py file defines what import *
will import. You can still force the import by giving the full name.

Example:
- Module alpacas/common/game_enums.py contains functions myfunc and secondfunc.
- In the module alpacas/__init__.py we have defined an import to the function myfunc:
      from alpacas.common.game_enums import myfunc
  This way we can just import myfunc directly from within the alpacas package without
  the need to know where that function resides.
- We ignore the secondfunc which of course could be imported like above.
- At the end of the alpacas/__init__.py module we define a list __all__ that only
  contains myfunc and not secondfunc. This means that an import * will only import
  myfunc and nothing else.
- When we now do am import * somewhere, like in this module, myfunc will be imported.
  When we try to run secondfunc it is not found.
- When we add a full import to the secondfunc we can still use the secondfunc.

When you comment the first line below (with import *) and uncomment the other two
import lines, both functions will be found.
When you run it like it is now, the secondfunc will not be found

'''


from alpacas import *
#from alpacas.common.game_enums import myfunc
#from alpacas.common.game_enums import secondfunc

myfunc()
#secondfunc()
printme()

class GameRoundSettings():
    ...

