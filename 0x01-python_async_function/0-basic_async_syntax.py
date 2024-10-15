#!/usr/bin/env python3
"""The Basics of async"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a delay, waits asynchronously for the delay
    and returns it finally.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
