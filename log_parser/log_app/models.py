from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True


class CreateMixin(models.Model):
    created = models.DateTimeField(verbose_name='Создано') # timestamp строки лога
    class Meta:
        abstract = True


class Message(BaseModel, CreateMixin):
    """
    Сообщения
    """
    in_log_id = models.CharField(max_length=20) # значение поля id=xxxx из строки лога
    int_id = models.CharField(max_length=128) # внутренний id сообщения
    log_str = models.TextField() # строка лога (без временной метки)
    # status = models.BooleanField() # пока не ясно

    def as_dict(self):
        return dict(
            int_id = self.int_id,
            created=self.created,
            log_str=self.log_str,
            address=''
        )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(BaseModel, CreateMixin):
    """
    Лог
    """
    int_id = models.CharField(max_length=128) # внутренний id сообщения
    log_str = models.TextField() # строка лога (без временной метки)
    address = models.CharField(max_length=128) # адрес получателя

    def as_dict(self):
        return dict(
            int_id = self.int_id,
            created=self.created,
            log_str=self.log_str,
            address=self.address
        )

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
