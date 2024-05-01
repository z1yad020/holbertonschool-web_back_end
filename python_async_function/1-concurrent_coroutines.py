#!/usr/bin/env python3

"""
basics
"""
from typing import List
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """random wait"""
    x = sorted([await wait_random(max_delay) for _ in range(n)])
    return x
