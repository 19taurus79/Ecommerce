# Ecommerce

## Если в проекте будут изображения, необходимо в файле setings.py добавить настройки

import os
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

### Необходимо именить файл urls.py
импортировать settings.py
from.django.conf.urls.static import static
к паттерну url добавить + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
