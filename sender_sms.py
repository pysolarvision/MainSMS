import aiohttp
import secrets
import hashlib


class LoginCodeSender:
    """"Класс отправки СМС-кода"""
    url: str = 'http://mainsms.ru/api/mainsms/message/send'
    headers: str = {'Accept': 'application/json'}

    def __init__(self, message: str, params):
        self.message = message
        self.params = params

    @staticmethod
    def generate_code() -> str:
        """"Функция генерирует 4-х значный код"""
        auth_code = ''.join(str(secrets.randbelow(10)) for _ in range(4))
        return auth_code

    @classmethod
    def hasher_code(cls, code: str) -> str:
        """"Функция хэширует 4-х значный код"""
        hashed_code = hashlib.sha256(code.encode()).hexdigest()
        return hashed_code

    async def send_code(self) -> None:
        """"Функция отправляет сгенерированный код"""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=self.headers, params=self.params) as response:
                print(response)
