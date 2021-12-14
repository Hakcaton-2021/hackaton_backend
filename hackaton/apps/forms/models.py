from django.db import models


class Forms(models.Model):
    """ Formularios de enrolamiento
    """
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=250, db_index=True)
    business_name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "forms"
