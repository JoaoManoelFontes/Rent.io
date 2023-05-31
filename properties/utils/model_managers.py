from django.db import models
from django.contrib.contenttypes.models import ContentType


class MediaManager(models.Manager):
    def filter(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        return super(MediaManager, self).filter(
            content_type=content_type, object_id=obj_id
        )


class PaymentManager(models.Manager):
    def filter(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        return super(PaymentManager, self).filter(
            content_type=content_type, object_id=obj_id
        )


class ContractManager(models.Manager):
    def filter(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        return super(ContractManager, self).filter(
            content_type=content_type, object_id=obj_id
        )
