from django.apps import AppConfig


class RedisTaskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'redis_task'
