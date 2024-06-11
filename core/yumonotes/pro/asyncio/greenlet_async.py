import asyncio

from greenlet import greenlet


class Coroutine:
    def __init__(self):
        pass

    def Greenlet(self):
        def func_0():
            print(1)
            gr1.switch()
            print(2)
            gr1.switch()

        def func_1():
            print(3)
            gr0.switch()
            print(4)

        gr0 = greenlet(func_0)
        gr1 = greenlet(func_1)

        gr0.switch()

    def Yield(self):
        def func_0():
            yield 1
            yield from func_1()
            yield 2

        def func_1():
            yield 3
            yield 4

        f0 = func_0()
        for item in f0:
            print(item)

    def Asyncio(self):
        @asyncio.coroutine
        def func_0():
            print(1)
            yield from asyncio.sleep(2)
            print(2)

        @asyncio.coroutine
        def func_1():
            print(3)
            yield from asyncio.sleep(2)
            print(4)

        taks = [
            asyncio.ensure_future(func_0()),
            asyncio.ensure_future(func_1())
        ]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait(taks))


if __name__ == '__main__':
    coroutine = Coroutine()
    # coroutine.Greenlet()
    # coroutine.Yield()
    coroutine.Asyncio()
