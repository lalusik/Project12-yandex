#Стулова Алла, когорта 24, Финальный проект. Инженер по тестированию плюс
import sending_requests
def get_trask_number_of_order():
    #Сохраняем ответ, при создании нового заказа
    track_number = sending_requests.post_new_order()
    #Сохраняем полученный трек
    return track_number.json()["track"]

def test_create_and_track_order():
    track_number = get_trask_number_of_order()
    #Сохраняем результат запроса на получение информации по треку
    get_response = sending_requests.get_order_info(track_number)
    #Проверка успешного получения заказа по треку
    assert get_response.status_code == 200