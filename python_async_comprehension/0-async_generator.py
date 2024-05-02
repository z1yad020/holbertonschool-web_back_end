#!/usr/bin/env python3

"""
comprehension
"""
from typing import Generator
import time
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """random wait"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
