from utils.utils import digit_wise_sum

from typing import Any, Tuple

import numpy as np
import math

class Prover:
    def __init__(self, id: Any, p: int, alpha: int, private_key: int):
        self.__id : Any = id
        self.p : int = p
        self.alpha : int = alpha
        self.__private_key : int = private_key
        self.public_key : int = pow(self.alpha, self.__private_key, self.p)

    # STEP 1 for the proposal challenge-response schema
    def send_id(self) -> Any:
        return self.__id

    # STEP 3 for the proposal challenge-response schema
    def __resolve_challenge(self, challenge: int) -> Tuple[int, int]:
        r = None

        while r is None or math.gcd(r, (self.p - 1)) != 1:
            r = digit_wise_sum(np.random.randint(self.p))

        t1 = pow(self.alpha, r, self.p)
        t2 = (challenge - (self.public_key * t1) * pow(r, -1, self.p)) % (self.p - 1)

        return t1, t2

    def send_response(self, challenge: int) -> Tuple[int, int]:
        return self.__resolve_challenge(challenge)
