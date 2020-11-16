<<<<<<< HEAD
=======
from pprint import pprint

>>>>>>> 0f777cf21f312c7a0d1d0233812eeb6117862446
import vk_api


class VkUser:

    def __init__(self):
        self.token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
<<<<<<< HEAD
        self.vk_api = vk_api.VkApi(token=self.token).get_api()
        self.photo_info_dict = {}
        self.tmp = {}

    def get_user_info(self, user_id):
        """
        :param user_id: принимает User ID или Короткое название аккаунта VK
        :return: словарь со информацией о Юзере (Имя, Фамилия, Id, пол, день рождеждения, город(id, название)
        """
        user = self.vk_api.users.get(user_ids=user_id, fields='first_name, last_name, sex, bdate, city')
        return user[0]

    def get_users_best_photos(self, user_id, count_photos=3):
        """
        Получаем словарь с ТОП фотографиями из профиля
        :param count_photos: количество фотографий с максимальными лайками
        :param user_id: принимает User ID или Короткое название аккаунта VK
        :return: словарь с ТОП 3мя фотографиями (ссылки (значения))
        из профиля аккаунта с их лайками (в качетстве имени (ключ))
        """
        photos_info = self.vk_api.photos.get(owner_id=self.get_user_info(user_id)['id'], album_id='profile',
                                             extended=1, count=1000, photo_sizes=0)
        # создаем словарь со всеми лайками и ссылками на фото
        for elem in photos_info['items']:
            photo_url = elem['sizes'][-1]['url']
            photos_list_likes = elem['likes']['count']
            if photos_list_likes in self.photo_info_dict:
                self.tmp[photos_list_likes - 1] = photo_url
            self.tmp[photos_list_likes] = photo_url
        # новый словарь с необходимым количеством максимальных лайков
        self.photo_info_dict = {k: v for k, v in self.tmp.items() if
                                k > sorted(self.tmp.keys(), reverse=True)[count_photos]}
        return self.photo_info_dict

    def get_city_id(self, city):
        """
        Принимает название города или его id и выдает id города
        :param city: Название города, можно часть или id
        :return: id города
        """
        try:
            int(city)
            return city
        except ValueError:
            city_id = self.vk_api.database.getCities(country_id=1, q=city)
            return city_id['items'][0]['id']

    def search_dating_user(self, age_from, age_to, sex, city, relation):
        """
        Получаем словарь с результатами поиска для дальнейшего просмотра людей
        :param age_from:    возраст, от.
        :param age_to:      возраст, до.
        :param sex:         пол                 (1 — женщина;
                                                 2 — мужчина)
        :param city:        город (id или название)
        :param relation:    семейное положение (1 — не женат/не замужем;
                                                2 — есть друг/есть подруга;
                                                3 — помолвлен/помолвлена;
                                                4 — женат/замужем;
                                                5 — всё сложно;
                                                6 — в активном поиске;
                                                7 — влюблён/влюблена;
                                                8 — в гражданском браке;
                                                0 — не указано)
        :return:            словарь с подходящими Юзерами
        """
        users_info_dict = self.vk_api.users.search(count=1000, age_from=age_from, age_to=age_to,
                                                   sex=sex, city=self.get_city_id(city), relation=relation,
                                                   fields='bdate')

        return users_info_dict['items']


if __name__ == '__main__':
    pass
=======
        self.vk_api = vk_get_api = vk_api.VkApi(token=self.token).get_api()

    def get_user_info(self, user_id):
        user = self.vk_api.users.get(user_ids=user_id, fields='first_name, last_name, sex, bdate')
        return user[0]

    # def get_profile_photos(self, album_id="profile"):
    #     profile_photos_info_list = []
    #     downloaded_files = []
    #     url = f"https://api.vk.com/method/photos.get"
    #     parameters = {
    #         "owner_id": self.id,
    #         "album_id": album_id,
    #         "extended": 1,
    #         "photo_sizes": 1,
    #         "count": 5,
    #         "access_token": self.token,
    #         "v": 5.122
    #     }
    #     url_requests = "?".join((url, urlencode(parameters)))
    #     resp = requests.get(url_requests)
    #     self.photo_list = resp.json()["response"]["items"]

    def get_users_best_photos(self, user_id):
        parameters = {
            "owner_id": user_id,
            "extended": 1,
            "photo_sizes": 0,
            "count": 200,
            "access_token": self.token,
            "v": 5.77
        }
        photos_info = self.vk_api.photos.get(owner_id=user_id, album_id='profile',
                                             extended=1, count=1000, photo_sizes=0)
        photos_list = [elem['likes']['count'] for elem in photos_info['items']]

        return photos_list


if __name__ == '__main__':
    print(VkUser().get_user_info(206241))
    pprint(VkUser().get_users_best_photos(206241))

>>>>>>> 0f777cf21f312c7a0d1d0233812eeb6117862446
