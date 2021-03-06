# Stubs for gdb.function.caller_is (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import gdb
from typing import Any

class CallerIs(gdb.Function):
    def __init__(self) -> None: ...
    def invoke(self, name: Any, nframes: int = ...): ...

class CallerMatches(gdb.Function):
    def __init__(self) -> None: ...
    def invoke(self, name: Any, nframes: int = ...): ...

class AnyCallerIs(gdb.Function):
    def __init__(self) -> None: ...
    def invoke(self, name: Any, nframes: int = ...): ...

class AnyCallerMatches(gdb.Function):
    def __init__(self) -> None: ...
    def invoke(self, name: Any, nframes: int = ...): ...
