from hackaton.apps.forms.models import Forms


class FormRepository:
    
    def create(self, data: dict):
        """
        """
        form = Forms.objects.create(**data)
        return form