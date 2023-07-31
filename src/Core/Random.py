from __future__ import annotations

from time import time
from typing import TYPE_CHECKING, Any, Dict, List, Optional

if TYPE_CHECKING:
    from Core import DMGame
################################################################################

__all__ = ("DMGenerator", )

################################################################################
class DMGenerator:

    __slots__ = (
        "_state",
        "_MT",
        "_index",
        "_seed",
    )

################################################################################
##### INITIALIZATION ###########################################################
################################################################################
    def __init__(self, state: DMGame, seed: Optional[int] = None) -> None:

        self._state: DMGame = state

        self._MT: List[int] = [0] * 624
        self._seed: Optional[int] = seed or int(time())
        self._MT[0] = self._seed

        self._index: int = 624

        self._generate_initial_array()

################################################################################
    def _generate_initial_array(self) -> None:

        for i in range(1, 624):
            self._MT[i] = (
                (0x6c078965 * (self._MT[i - 1] ^ (self._MT[i - 1] >> 30)) + i) & 0xFFFFFFFF
            )

################################################################################
##### INTERNAL METHODS #########################################################
################################################################################
    def _regenerate(self) -> None:

        for i in range(624):
            y = (self._MT[i] & 0x80000000) + (self._MT[(i + 1) % 624] & 0x7fffffff)
            self._MT[i] = self._MT[(i + 397) % 624] ^ (y >> 1)

            if y % 2 != 0:
                self._MT[i] ^= 0x9908b0df

        self._index = 0

################################################################################
    def _next(self) -> float:

        if self._index >= 624:
            self._regenerate()

        y = self._MT[self._index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= y >> 18

        self._index += 1

        return y / 0xffffffff

################################################################################
##### PUBLIC METHODS ###########################################################
################################################################################
    def choice(self, seq: List[Any], *, exclude: Optional[Any] = None) -> Any:

        if exclude is not None:
            seq = [item for item in seq if item != exclude]

        try:
            return seq[int(self._next() * len(seq))]
        except IndexError:
            return None

################################################################################
    def sample(self, seq: List[Any], n: int, *, exclude: Optional[Any] = None) -> List[Any]:

        if exclude is not None:
            seq = [item for item in seq if item != exclude]

        if n > len(seq):
            return []

        return [seq.pop(int(self._next() * len(seq))) for _ in range(n)]

################################################################################
    def weighted_choice(
        self,
        seq: List[Any],
        _weights: Dict[int, float],
        n: int,
        *,
        exclude: Optional[Any] = None
    ) -> Any:

        weights = [_weights.get(item.rank, 0) for item in seq]

        assert len(seq) == len(weights), "Array and weights must have the same length"
        assert all(weight >= 0 for weight in weights), "Weights must be non-negative"
        assert any(weight > 0 for weight in weights), "At least one weight must be positive"

        total_weight = sum(weights)
        scaled_weights = [weight / total_weight for weight in weights]

        choices = []
        for _ in range(n):
            r = self._next()
            for i, weight in enumerate(scaled_weights):
                if r < weight:
                    choices.append(seq[i])
                    break
                r -= weight

        return choices

################################################################################
    def from_range(self, start: float, stop: float) -> float:

        def frange(begin, end):
            i = begin
            while i < end:
                yield i
                i += 0.01

        return self.choice([i for i in frange(start, stop + 1)])

################################################################################
    def chance(self, chance: float) -> bool:

        if chance not in range(0, 101):
            raise ValueError("Chance must be between 0 and 100")

        if chance > 1:
            chance /= 100
        elif chance < 0:
            chance = 0

        return self._next() <= chance

################################################################################
