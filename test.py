import asyncio
import time

# 1. 用异步生成器替代类实现的异步迭代器
async def async_counter(limit):
    count = 0
    while count < limit:
        count += 1
        # 模拟异步操作
        await asyncio.sleep(0.5)
        yield count  # 异步生成下一个值

# 2. 返回异步迭代器（这里直接返回异步生成器，它本身就是异步迭代器）
async def get_async_iterator(limit):
    # 获取生成器
    print("创建异步迭代器...")
    return async_counter(limit)  # 返回异步生成器

# 3. 在调用栈中使用
async def process_data():
    # 中间层
    print("获取异步迭代器...")
    async_iterator = await get_async_iterator(5)  # 获取异步迭代器
    
    print("开始迭代数据...")
    async for item in async_iterator:  # 同样使用async for遍历
        print(f"处理数据: {item}")

# 4. 主函数
async def main():
    start_time = time.time()
    await process_data()
    print(f"总耗时: {time.time() - start_time:.2f}秒")

if __name__ == "__main__":
    asyncio.run(main())
    