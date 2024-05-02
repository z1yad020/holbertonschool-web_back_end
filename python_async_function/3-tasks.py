#!/usr/bin/env python3

"""
basics
"""
from typing import List
import time
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """random wait"""
    return asyncio.Task(wait_random(max_delay))
