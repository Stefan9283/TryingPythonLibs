#! /usr/bin/python3


import asyncio


async def partial_sum(start: int, end: int):
    sum = 0
    for i in range(start,end):
        sum+=i
    return sum



async def efficient_sum(to_value, parts_num):
    sum = 0
    step = int(to_value/parts_num)
    futures = []

    if step < 1:
        step = 1

    last_right_value = 0

    for i in range(0, to_value+1-step, step):
        last_right_value = i + step
        futures.append(asyncio.ensure_future(partial_sum(i, i+step)))
    
    futures.append(asyncio.ensure_future(partial_sum(last_right_value, to_value+1)))

    value = await asyncio.gather(*futures)

    print(value)
    
    for i in value:
        sum += i


    return sum


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    r = loop.run_until_complete(efficient_sum(1000,3))
    print(r)
    loop.close()
