#! /usr/bin/python3


import asyncio


should_i_be_running = True


async def my_print(string):
    while should_i_be_running == True:
        print(string)
        #await asyncio.sleep(0.3)
        await asyncio.sleep(0.5)

async def test():

    task = []


    task.append(asyncio.create_task(my_print("hi")))
    task.append(asyncio.create_task(my_print("hello")))
    #task.append(asyncio.ensure_future(my_print("hi")))
    #task.append(asyncio.ensure_future(my_print("hello")))

    print(task)
    print("########################")


    #responses = await asyncio.gather(*task)

    

    input("Insert anything to stop\n")
    should_i_be_running = False

    responses = []

    responses.append(task[0].result)
    responses.append(task[1].result)


    print(should_i_be_running)
    return responses


#async def main():
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(test())
loop.run_until_complete(future)
responses = future.result()


#asyncio.run(main())