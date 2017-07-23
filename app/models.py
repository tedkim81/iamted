import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

def profile_upload_path(instance, filename):
    return os.path.join('profile', str(instance.id), filename)
