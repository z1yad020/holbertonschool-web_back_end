#!/usr/bin/env python3

"""
basics
"""
from typing import List
import time
import asyncio
import random


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """random wait"""
    x = sorted([await task_wait_random(max_delay) for _ in range(n)])
    return x
