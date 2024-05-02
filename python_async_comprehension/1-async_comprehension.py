#!/usr/bin/env python3

"""
comprehension
"""
from typing import List
import time
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """random wait"""
    return [i async for i in async_generator()]
