# Django-приложение для парсинга уязвимостей и сканирования

## Обзор

Это приложение на основе Django представляет собой универсальный инструмент для специалистов по кибербезопасности. Оно сочетает в себе возможности веб-скрапинга и сетевого сканирования для:

- Парсинга уязвимостей и эксплойтов с сайта [Sploitus](https://sploitus.com).
- Сканирования IP-адресов на наличие уязвимостей с использованием Nmap.

## Возможности

### 1. **Парсинг уязвимостей и эксплойтов**
   - Получение актуальной информации об уязвимостях и эксплойтах с Sploitus.
   - Сохранение данных в структурированном виде в базе данных для удобного поиска.
   - Поддержка фильтрации и поиска уязвимостей по CVE, дате или уровню опасности.

### 2. **Сканирование IP-адресов с Nmap**
   - Выполнение сетевого сканирования указанных IP-адресов или диапазонов.
   - Определение открытых портов, запущенных сервисов и потенциальных уязвимостей.
   - Генерация подробных отчетов в удобном формате.

### 3. **Веб-интерфейс**
   - Интуитивно понятный интерфейс для управления сканами и просмотра результатов.
   - Обновление статуса выполнения задач в реальном времени.

### 4. **API-интеграция**
   - RESTful API для программного доступа к данным о уязвимостях и результатам сканирования.
   - Обеспечивает интеграцию с другими инструментами и процессами.

## Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Gleb4ik2001/security_hacathon.git
   cd security_hacathon
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3. Создайте миграции:
   ```bash
   python manage.py makemigrations
   ```

4. Примените миграции:
   ```bash
   python manage.py migrate
   ```

5. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

6. Откройте приложение по адресу `http://127.0.0.1:8000`.

## Использование

### Парсинг уязвимостей
1. Перейдите в раздел "Парсинг уязвимостей".
2. Нажмите "Получить данные" для парсинга актуальной информации с Sploitus.
3. Просматривайте результаты в панели управления.

### Сканирование IP
1. Перейдите в раздел "Сканер IP".
2. Укажите IP-адрес или диапазон для сканирования.
3. Запустите сканирование и следите за прогрессом в реальном времени.
4. После завершения просматривайте подробные результаты.

## Настройка

- **Настройки базы данных**: Конфигурация базы данных выполняется в `settings.py`.
- **Путь к Nmap**: Убедитесь, что Nmap установлен и доступен в PATH системы.
- **Планировщик задач**: Используйте `django-cron` или аналогичный пакет для автоматизации периодического парсинга и сканирования.

## Требования

- Python 3.8+
## Безопасность

- Всегда выполняйте сканирование только на авторизованных сетях.
- Соблюдайте этические принципы и получайте разрешение перед сканированием сторонних систем.
- Используйте HTTPS для защиты связи между клиентом и сервером.

## Участие в проекте

Приветствуются любые предложения и улучшения! Открывайте issue или создавайте pull request, чтобы сообщить об ошибках или предложить новые функции.


Удачного сканирования и будьте в безопасности!
