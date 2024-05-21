import aiohttp
import asyncio


class Fetch:
    server_url = "http://127.0.0.1"

    @classmethod
    async def fetch(cls, session, url, method='get', data=None):
        async with session.request(method, url, data=data) as response:
            return await response.json()

    @classmethod
    async def registrate_user(cls, user_id: str):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/user/registrate", 'post', {"user_id": user_id})
                return response.get("message")
            except:
                return {"message": "something went wrong"}

    @classmethod
    async def login_user(cls, user_id: str):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/user/login", 'get', {"user_id": user_id})
                return response.get("message")
            except:
                return {"message": "something went wrong"}

    @classmethod
    async def get_user(cls, user_id: str):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/user/", 'get', {"user_id": user_id})
                return response.get("message")
            except:
                return {"message": "something went wrong"}

    @classmethod
    async def add_tag_user(cls, tag: str):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/user", 'put', {"tag": tag})
                return response.get("message")
            except:
                return {"message": "something went wrong"}

    @classmethod
    async def group(cls, tag: str):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/groups", 'get', {"tag": tag})
                message = response.get("message")
                message["images"] = [await cls.fetch(session, cls.server_url + "/static/img/" + image, 'get') for image in message["images"]]
                return message
            except:
                return {"message": "something went wrong"}

    @classmethod
    async def tags(cls):
        async with aiohttp.ClientSession() as session:
            try:
                response = await cls.fetch(session, cls.server_url + "/api/tags", 'get')
                return response.get("message")
            except:
                return {"message": "something went wrong"}
