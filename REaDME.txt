Python 3.4.5
Django 1.8

ammenv\ -- виртуальное окружение. под ним всё настроено и работает по крайней мере точно
чтобы запустить окружение под виндой должно сработать в консоли находясь в текущей папке:
> ammenv\Scripts\activate

ammsite\ -- рабочая папка
	ammapp\ --  папка приложения
		templates\ammapp\ -- готовые html-шаблоны
		admin.py -- файл регистрации моделей
		models.py -- файл моделей
		views.py -- представления
	ammsite\ -- общая папка проекта
		settings.py -- настройки и регистрация приложения
		urls.py -- роутинг
	manage.py -- основной файл манипуляций с проектом
		подтверждение изменений в файлах:
		> python manage.py makemigrations ammapp 
		загрузка в базу данных:
		> python manage.py migrate ammapp
		запуск сервера:
		> python manage.py runserver
		создание суперюзверя(уже создан по идее логин/паcc admin/admin):
		> python manage createsuperuser
		
после запуска сервера:
127.0.0.1:8000/admin -- админка
в ней наполняятся ручками БД
127.0.0.1:8000/ammapp -- главная страница приложения

	

