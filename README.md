# Ecommerce
https://youtu.be/bFsIXYygsg4?si=5xy7eYH2FZe2fQnb
## Если в проекте будут изображения, необходимо в файле setings.py добавить настройки

import os
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
для статических фалов необходимо прописать
STATICFILES_DIRS = ['static/']

### Необходимо именить файл urls.py
импортировать settings.py
from.django.conf.urls.static import static
к паттерну url добавить + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

### Шаблоны для сайтов
https://startbootstrap.com/
в файле html загрузить статические файлы {% static %}  
в ссылках на статические файлы необходимо прописать :
{% static '<путь>' %}