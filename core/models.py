from django.db import models


class EmailList(models.Model):
    name = models.CharField(max_length=50)
    email_address = models.EmailField()
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '%s for: %s' % (self.name, self.email_address)
