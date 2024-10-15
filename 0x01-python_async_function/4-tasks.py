#!/usr/bin/env python3
"""
Executing multiple coroutines at a time.
"""
import asyncio
from typing import List, Callable


task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except
    task_wait_random is being called.
    """
    delays = await asyncio.gather(*(
        task_wait_random(max_delay) for _ in range(n)
        ))
    result: List[float] = []
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
