import vk_api.vk_api

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from commander import Commander


class Server:
    def __init__(self, api_token, group_id, server_name: str="noname"):
        self.server_name = server_name
        self.vk = vk_api.VkApi(token=api_token)
        self.long_poll = VkBotLongPoll(self.vk,group_id)
        self.vk_api = self.vk.get_api()
        print("Сервер " + self.server_name + " запущен!")
        self.users = {}

    def send_msg(self,send_id,message):
        self.vk_api.messages.send(peer_id=send_id,
                                  message=message,
                                  random_id = get_random_id())

    def test(self,id):
        self.send_msg(id,"Testing")

    def start(self):
        for event in self.long_poll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                if event.object.from_id not in self.users:
                    self.users[event.object.from_id] = Commander()

                self.send_msg(event.object.peer_id, self.users[event.object.from_id].ans(event.object.text))

    def get_user_name(self, user_id):
        return self.vk_api.users.get(user_id=user_id)[0]['first_name']

    def mainloop(self, exception=0):
        if exception >10:
            print("Произошло больше 10 ошибок. Отключаю сервер...")
            return

        try:
            self.start()
        except Exception as e:
            print("Произошла ошибка! Перезапускаю сервер! Ошибка:"+e.__str__())
            self.mainloop(exception+1)

