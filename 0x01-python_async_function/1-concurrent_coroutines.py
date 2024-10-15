#!/usr/bin/env python3
"""
Executing multiple coroutines at a time.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Gets delay for tasks processing asynchronously
    and returns a sorted list of the delays
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        if len(delays) == 0:
            delays.append(delay)
        else:
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    break
                else:
                    delays.append(delay)
    return delays
