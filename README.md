# Проект автоматизации тестирования сервиса StellarBurger: API

1. Основа для написания автотестов — фреймворк pytest и библиотека для работы с HTTP запросами Requests.
2. Подготовка отчетов тестирования выполнена с помощью фреймворка Allure.
3. Установить зависимости — pip install -r requirements.txt.
4. Команда для запуска тестов — pytest -v.
5. Команда для формирования Allure-отчета — pytest --alluredir=allure_results.
6. Команда для формирования отчета в виде web-страницы — allure serve allure_results, где allure_results - папка с файлами отчета.

## Описание файлов с тестами
* test_user_registration.py - проверка регистрации пользователя
* test_user_login.py - проверка авторизации пользователя
* test_create_order.py - проверка создания заказа
* test_change_user_datas.py - проверка изменения данных пользователя
* test_get_user_order.py - проверка получения заказов конкретного пользователя 

## Описание вспомогательных файлов
* conftest.py - используемые фикстуры
* helpers.py - вспомогательные функции
* stellar_burger.py - API запросов
* Urls.py - адреса API