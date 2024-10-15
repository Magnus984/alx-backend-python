#!/usr/bin/env python3
"""Creates Tasks"""
import asyncio
from typing import Callable

wait_random: Callable = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an integer and returns a task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
