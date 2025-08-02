# 异步迭代器
### 定义迭代器
##### 异步迭代器函数: async + yield
```python
async def async_iterable(n):
    for i in range(n):
        yield i
```
##### 异步迭代器类实现: aiter + anext
```python
class AsyncIterable:
    """异步数据获取器，作为异步迭代器的示例"""
    
    def __init__(self, max_items: int):
        self.max_items = max_items  # 最大迭代次数
        self.current = 0  # 当前迭代位置

    # 实现异步迭代器协议：返回自身作为迭代器
    def __aiter__(self):
        return self

    # 实现异步迭代器协议：返回下一个异步值
    async def __anext__(self):
        # 迭代终止条件：达到最大次数时抛出StopAsyncIteration
        if self.current >= self.max_items:
            raise StopAsyncIteration

        # 模拟异步操作（如网络请求、数据库查询等）
        await asyncio.sleep(random.uniform(0.1, 0.5))  # 随机延迟模拟IO操作
        
        # 生成数据
        self.current += 1
        return f"数据项 #{self.current} (延迟: {random.uniform(0.1, 0.5):.2f}s)"
```
### 传递迭代器
* 将异步迭代器作为返回值，在调用堆栈中传递的过程中， 不能使用 async for 或者 aiter & anext 访问迭代器
* 获取迭代器对象， 创建迭代器对象，但不做访问, 而是作为返回值传递给外部
```python
# 获取迭代器
async def getIter():
    return async_iterable(100)
    # return await asynciterable === X
```
* await 调用获取迭代器函数， 传递异步迭代器对象。 (异步函数直接调用返回的是协程对象，使用await调用协程对象，执行代码，返回迭代器)
```python
# 遍历迭代器
async def main():
    asynciter = await getIter()
    async for item in asynciter:
        print("当前遍历元素：", item)
```