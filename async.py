import asyncio

async def random(word, delay):
    await asyncio.sleep(delay)
    print(word)
    
async def main():
    await asyncio.gather(
    random("телефон", 1),
    random("компьютер", 2),
    random("собака", 3),
    random("сумка", 1),
    random("духи", 3),
    random("косметика", 2), 
    random("крабик", 1),
    random("чехол", 3),
    random("резинка", 2),
    random("кот", 1))
    
asyncio.run(main())
