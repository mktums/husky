# Тестовое задание для HuskyJam
> Веб-страница с формой записи к врачу в поликлинике. Пользователь должен иметь возможность выбрать в форме время, дату и врача, указать свои ФИО и отправить данные. Прием длится один час, нет возможности выбрать у врача время, на которое кто-либо уже записался. Так же нет возможности записаться в нерабочее время. Время работы поликлиники: пн - пт с 9:00 до 18:00. Администратор может зайти через админку и посмотреть запись у любого врача.
>
> Результат должен быть выложен на гитхаб и запускаться на Python 3.x и Django 1.8.
>
> Дополнительное задание по желанию:
> 
> Тестовый запуск будет производиться на чистом окружении Ubuntu Server 14.04 x64 при помощи скрипта start.sh, который должен быть расположен в корне проекта. Скрипт будет вызван из папки проекта пользователем с root правами и должен произвести установку всех необходимых пакетов, в том числе интерпретатора Python 3-й и самого фреймворка Django. После выполнения скрипта приложение должно быть доступно на 0.0.0.0:80.
