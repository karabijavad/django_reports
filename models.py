from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User


class ReportUserProfile(TimeStampedModel):
    user = models.ForeignKey(User, unique=True)
