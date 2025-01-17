from django.shortcuts import render
from django.contrib import messages
from easyAPI import settings
from django.http import JsonResponse
import httpx
import json

def index(request):
    """
    Отображает главную страницу сайта.
    """
    return render(request, 'index.html')

def api_exotic_flowers(request):
    if request.method == 'POST':
        try:
            data = {
                "user": {
                    "full_name": "John Doe",
                    "contact_info":{
                        "email": "john.doe@example.com",
                        "phone": "+1234567890"
                        },
                    },
                "application": {
                    "created_at": "2015-12-01T00:00:00",
                    "product_name": "Exotic Flower",
                    "product_quantity": 10,
                    "delivery_time": "01.04.2025",
                    "payment_method": "Credit Card",
                    }
                }
            url = "http://127.0.0.1/exotic_flowers/hs/applicationData/get_application/"
            auth = (settings.ONEC_API_USER, settings.ONEC_API_PASSWORD)  # Логин и пароль
            
            with httpx.Client() as client:
                headers = {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept': 'application/json'
                    }
                response = client.post(
                    url,
                    json=data,
                    headers=headers,
                    auth=(auth[0], auth[1]),  # Авторизация
                    timeout=10  # Таймаут для запроса
                )

            if response.status_code == 200:
                messages.success(request, 'Вы успешно подтвердили заявку. Информация отправлена в 1С.')
            else:
                messages.warning(request, f'Заявка подтверждена, но данные в 1С не отправлены. Ошибка: {response.text}')
        except httpx.RequestError as e:
            messages.error(request, f'Ошибка при отправке данных в 1С: {str(e)}')   
def api_photo_salon (request):
    if request.method == 'POST':
        try:
            data = {
                "user": {
                    "full_name": "John Doe",
                    "contact_info":{
                        "email": "john.doe@example.com",
                        "phone": "+1234567890"
                        },
                    },
                "application": {
                    "created_at": "2015-12-01T00:00:00",
                    "filming_location": "Hollywood",
                    "people_quantity": 10,
                    "desired_date": "01.04.2025",
                    }
                }
            url = "http://127.0.0.1/photo_salon/hs/applicationData/get_application/"
            auth = ("Дмитрий", "")  # Логин и пароль
            
            with httpx.Client() as client:
                headers = {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept': 'application/json'
                    }
                response = client.post(
                    url,
                    json=data,
                    headers=headers,
                    auth=(auth[0], auth[1]),  # Авторизация
                    timeout=10  # Таймаут для запроса
                )

            if response.status_code == 200:
                messages.success(request, 'Вы успешно подтвердили заявку. Информация отправлена в 1С.')
            else:
                messages.warning(request, f'Заявка подтверждена, но данные в 1С не отправлены. Ошибка: {response.text}')
        except httpx.RequestError as e:
            messages.error(request, f'Ошибка при отправке данных в 1С: {str(e)}')

def api_production_center(request):
    if request.method == 'POST':
        try:
            data = {
                "user": {
                    "full_name": "John Doe",
                    "contact_info":{
                        "email": "john.doe@example.com",
                        "phone": "+1234567890"
                        },
                    },
                "application": {
                    "created_at": "2015-12-01T00:00:00",
                    "purpose_appeal": "",
                    "self_presentation": "",
                    "files": "http://127.0.0.1:8000/media/barbariki_smile.mp3",
                    }
                }
            url = "http://127.0.0.1/production_center/hs/applicationData/get_application/"
            auth = ("Анастасия", "")  # Логин и пароль
            
            with httpx.Client() as client:
                headers = {
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept': 'application/json'
                    }
                response = client.post(
                    url,
                    json=data,
                    headers=headers,
                    auth=(auth[0], auth[1]),  # Авторизация
                    timeout=10  # Таймаут для запроса
                )

            if response.status_code == 200:
                messages.success(request, 'Вы успешно подтвердили заявку. Информация отправлена в 1С.')
            else:
                messages.warning(request, f'Заявка подтверждена, но данные в 1С не отправлены. Ошибка: {response.text}')
        except httpx.RequestError as e:
            messages.error(request, f'Ошибка при отправке данных в 1С: {str(e)}')