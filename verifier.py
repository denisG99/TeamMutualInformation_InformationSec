from typing import Tuple

import numpy as np

class Verifier:
    def __init__(self, p: int, alpha: int, prover_public_key: int):
        self.p : int = p
        self.alpha : int = alpha
        self.prover_public_key : int = prover_public_key
        self.__challenge : int|None = None # ASSUMPTION: we assume that verifier handle only one prover at the time

    # STEP 2 for the proposal challenge-response schema
    def __create_challenge(self) -> None:
        self.__challenge = np.random.randint(self.p)

    def send_challenge(self) -> int:
        return self.__challenge

    # STEP 4 for the proposal challenge-response schema
    def __authentication(self, response: Tuple[int, int]) -> Tuple[int, int]:
        s = pow(self.alpha, self.__challenge, self.p)
        s_hat = (pow(self.prover_public_key, response[0]) * pow(response[0], response[1])) % self.p

        return s, s_hat

    def is_authenticated(self, response: Tuple[int, int]) -> bool:
        authentication = self.__authentication(response)

        return authentication[0] == authentication[1]