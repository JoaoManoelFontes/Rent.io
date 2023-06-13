from django.db import models
from django.contrib.contenttypes.models import ContentType


class GenericModelManager(models.Manager):
    def filter(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        return super(GenericModelManager, self).filter(
            content_type=content_type, object_id=obj_id
        )
