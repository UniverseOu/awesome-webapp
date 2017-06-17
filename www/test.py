import orm,asyncio,time
from models import User, Blog, Comment

async def test(loop):

	await orm.create_pool(loop=loop,user='root', password='root', db='awesome')
	summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	
	b = Blog( id = '5',user_id = '152565',user_name = 'Oceanb7',user_image = 'ssddf',
	name = 'oceanb',summary = summary,content = 'what the fuck ya',created_at = time.time())

	await b.save()
	await orm.destory_pool()
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()