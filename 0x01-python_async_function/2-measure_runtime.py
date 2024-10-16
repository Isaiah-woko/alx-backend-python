#!/usr/bin/env python3
"""This module is for task 2"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes average wait time"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
