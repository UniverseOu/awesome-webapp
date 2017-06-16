import orm,asyncio
from model import User, Blog, Comment

async def test(loop):

    await orm.create_pool(loop=loop,user='root', password='root', database='awesome')
    u = User(id='236794',name='ggg', email='ggg@example.com', passwd='0954321', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()