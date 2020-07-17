import datetime
import uuid

from django.core.exceptions import ValidationError
from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

# 3rd party apps
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# When time zone support is enabled (USE_TZ=True), Django uses time-zone-aware datetime objects.
# If your code creates datetime objects, they should be aware too
# same as datetime.datetime.now()
now = timezone.now()


def thumbnail_path(instance, filename):
    # checks jpg exttension
    extension = filename.split('.')[1]
    unique_name = uuid.uuid4().hex
    print('thumbnail_path/' + unique_name + '.' + extension)

    return 'thumbnail_path/' + unique_name + '.' + extension


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    thumbnail_img = models.ImageField(upload_to=thumbnail_path, max_length=52)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField('Date and Time', auto_now= True)
    created_on = models.DateTimeField(auto_now_add=False)
    status = models.IntegerField('Status', choices=STATUS, default=0)
    # implementing ckeditor app's richtextfield on content
    content = RichTextField()


    # validating created_on, so that user cannot select past date
    def clean(self):
        " Make sure expiry time cannot be in the past "
        if self.created_on and self.created_on < now:
            raise ValidationError('Please, pick present date and time...')

        # Don't allow draft entries to have a pub_date.
        # below code works fine, but not applicable here, as datefield is required here.
        # ref - https://docs.djangoproject.com/en/dev/ref/models/instances/#django.db.models.Model.clean_fields
        # if self.status == 'Draft' and self.created_on is not None:
        #     raise ValidationError(_('Draft posts may not have a publication date.'))
        #
        # # Set the pub_date for published items if it hasn't been set already.
        # if self.status == 'Publish' and self.created_on is None:
        #     self.pub_date = datetime.date.today()


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title