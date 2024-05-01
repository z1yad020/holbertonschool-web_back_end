#!/usr/bin/env python3

"""
basics
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """random wait"""
    f: float = random.uniform(0, max_delay)
    await asyncio.sleep(f)
    return f
