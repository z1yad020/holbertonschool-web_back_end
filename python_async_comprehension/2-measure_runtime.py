#!/usr/bin/env python3

"""
comprehension
"""
from typing import List
import time
import asyncio
import random

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """random wait"""
    f = async_comprehension
    s = time.perf_counter()

    total_runtime_list = [f(), f(), f(), f()]
    total_runtime_list = await gather(*total_runtime_list)

    elapsed = time.perf_counter() - s
    return elapsed
