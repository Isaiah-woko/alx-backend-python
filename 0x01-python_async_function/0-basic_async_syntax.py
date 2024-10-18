#!/usr/bin/env python3
"""This module is for task 0"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay
        (included and float value) seconds and eventually returns it.
    """

    waiting = random.random() * max_delay
    await asyncio.sleep(waiting)
    return waiting
