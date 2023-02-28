#!/usr/bin/env python3

"""
https://www.youtube.com/watch?v=-UBDRX6bk-A
"""

from __future__ import annotations

import logging
import sys
from argparse import ArgumentParser
from enum import Enum

from colorama import Back, Fore, Style

log = logging.getLogger(__name__)


class SwitchState(Enum):
    OFF = f"{Back.BLACK}{Fore.LIGHTBLACK_EX}0{Style.RESET_ALL}"
    ON = f"{Back.WHITE}{Fore.BLACK}1{Style.RESET_ALL}"

    def toggle(self) -> SwitchState:
        return SwitchState.OFF if self is SwitchState.ON else SwitchState.ON

    def __repr__(self) -> str:
        return f"{self.value}"


def toggle_switches(previous_switch_states: list[SwitchState], step: int) -> list[SwitchState]:
    new_switch_states = []
    for i, current_state in enumerate(previous_switch_states):
        new_switch_states.append(current_state.toggle() if is_multiple_of(i + 1, step) else current_state)
    return new_switch_states


def is_multiple_of(n: int, m: int) -> bool:
    """Return True iff n is an even multiple of m."""
    return n % m == 0


def main():
    parser = ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    switch_states = [SwitchState(SwitchState.OFF)] * args.n
    log.debug(f"{0: 3}, {switch_states}")

    for i in range(args.n):
        switch_states = toggle_switches(switch_states, i + 1)
        log.debug(f"{i + 1: 3}, {switch_states}")

    lights_that_are_on = [i + 1 for i in range(args.n) if switch_states[i] is SwitchState.ON]
    print(lights_that_are_on)

    # Confirm the amazing pattern
    for i, value in enumerate(lights_that_are_on):
        assert value == (i + 1) * (i + 1)


if __name__ == "__main__":
    sys.exit(main())
