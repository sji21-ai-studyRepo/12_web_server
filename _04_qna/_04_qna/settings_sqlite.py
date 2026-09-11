from .settings import *

# 기존 SQLite 데이터를 내보낼 때만 사용하는 임시 설정이다.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
