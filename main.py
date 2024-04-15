import asyncio

from sender_sms import LoginCodeSender

if __name__ == "__main__":
    user_phone_number = 79112352248
    message = f'Ваш код для входа: {LoginCodeSender.generate_code()}'
    params = {'project': 'my_pet_project',
              'recipients': user_phone_number,
              'message': message,
              'apikey': 'da28690b94519aa48c145158b341a620'}

    sender = LoginCodeSender(message, params)
    asyncio.run(sender.send_code())
