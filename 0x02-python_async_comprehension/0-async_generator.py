#!/usr/bin/env python3

""" 0. Async Generator """
import asyncio
import random


async def async_generator() -> asyncio.Task:
    """yield"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(1, 10)
