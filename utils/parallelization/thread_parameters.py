import dataclasses
from typing import Callable, Tuple, Any, Dict


@dataclasses.dataclass
class ThreadParameters:
    target: Callable
    args: Tuple[Any, ...] = ()
    kwargs: Dict[str, Any] = dataclasses.field(default_factory=dict)
    daemon: bool = True
