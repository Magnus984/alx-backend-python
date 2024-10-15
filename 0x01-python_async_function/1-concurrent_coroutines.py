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
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    result = []
    for delay in delays:
        inserted = False
        for i in range(len(result)):
            if delay < result[i]:
                result.insert(i, delay)
                inserted = True
                break
        if not inserted:
            result.append(delay)

    return result
