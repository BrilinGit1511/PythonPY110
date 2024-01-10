from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseNotFound
from .models import DATABASE
from logic.services import filtering_category, view_in_cart, add_to_cart, remove_from_cart
def products_view(request: HttpRequest):
    query_id = request.GET.get("id")
    if query_id:
        return JsonResponse(DATABASE[query_id], json_dumps_params={'ensure_ascii': False, 'indent': 4})
    else:
        return JsonResponse(DATABASE,  json_dumps_params={'ensure_ascii': False, 'indent': 4})
        # как в приложении app_weather
    if id_product := request.GET.get("id"):
        if data := DATABASE.get(id_product):
            return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                         'indent': 4})
        return HttpResponseNotFound("Данного продукта нет в базе данных")

        # Обработка фильтрации из параметров запроса
    category_key = request.GET.get("category")  # Считали 'category'
    if ordering_key := request.GET.get("ordering"):  # Если в параметрах есть 'ordering'
        if request.GET.get("reverse") in ('true', 'True'):  # Если в параметрах есть 'ordering' и 'reverse'=True
            data = ...  # TODO Провести фильтрацию с параметрами
        else:
            data = ...  # TODO Провести фильтрацию с параметрами
    else:
        data = ...  # TODO Провести фильтрацию с параметрами
    # В этот раз добавляем параметр safe=False, для корректного отображения списка в JSON
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False,
                                                             'indent': 4})

    return HttpResponseNotFound("Данного продукта нет в базе данных")

def shop_view(request):
    if request.method == "GET":
        with open('store/shop.html', encoding="utf-8") as f:
            data = f.read()  # Читаем HTML файл
        return HttpResponse(data)  # Отправляем HTML файл как ответ


def products_page_view(request, page):
    if request.method == "GET":
        for data in DATABASE.values():
            if isinstance(page, str):
                 if data['html'] == page:  # Если значение переданного параметра совпадает именем html файла
                     # TODO 1. Откройте файл open(f'store/products/{page}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
                     with open('store/products/{page}.html', encoding="utf-8") as f:
                     # TODO 2. Прочитайте его содержимое
                         data = f.read()
                     # TODO 3. Верните HttpResponse c содержимым html файла
                     return HttpResponse(data)
                     # Если за всё время поиска не было совпадений, то значит по данному имени нет соответствующей
                     # страницы товара и можно вернуть ответ с ошибкой HttpResponse(status=404)
            elif isinstance(page, int):
                data = DATABASE.get(str(page))  # Получаем какой странице соответствует данный id
                if data:  # Если по данному page было найдено значение
                     # 1. Откройте файл open(f'store/products/{data["html"]}.html', encoding="utf-8") (Не забываем про контекстный менеджер with)
                     with open('store/products/{data["html"]}.html', encoding="utf-8") as f:
                     # 2. Прочитайте его содержимое
                         data = f.read()
                     # 3. Верните HttpResponse c содержимым html файла
                     return HttpResponse(data)
        return HttpResponse(status=404)

def cart_view(request):
    if request.method == "GET":
        data = ... # TODO Вызвать ответственную за это действие функцию
        return JsonResponse(data, json_dumps_params={'ensure_ascii': False,
                                                     'indent': 4})


def cart_add_view(request, id_product):
    if request.method == "GET":
        result = ... # TODO Вызвать ответственную за это действие функцию
        if result:
            return JsonResponse({"answer": "Продукт успешно добавлен в корзину"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное добавление в корзину"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})


def cart_del_view(request, id_product):
    if request.method == "GET":
        result = ... # TODO Вызвать ответственную за это действие функцию
        if result:
            return JsonResponse({"answer": "Продукт успешно удалён из корзины"},
                                json_dumps_params={'ensure_ascii': False})

        return JsonResponse({"answer": "Неудачное удаление из корзины"},
                            status=404,
                            json_dumps_params={'ensure_ascii': False})




# Create your views here.
