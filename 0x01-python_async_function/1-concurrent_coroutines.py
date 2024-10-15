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
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    sorted_delays = []
    for delay in delays:
        if len(sorted_delays) == 0:
            sorted_delays.append(delay)
        else:
            for i in range(len(sorted_delays)):
                if delay < sorted_delays[i]:
                    sorted_delays.insert(i, delay)
                    break
                else:
                    sorted_delays.append(delay)
    return sorted_delays
