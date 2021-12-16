from hackaton.apps.forms.notifications import Notifications
from hackaton.apps.forms.models import Forms
from hackaton.settings.base import URL

class  CreateFormCase:
    
    def __init__(self, repository):
        self.repository = repository
    
    def set_params(self, data):
        self.data = data
    
    def execute(self):
        self.validation()
        form = self.repository.create(self.data)
        notify = Notifications(send_email=True, template='email/initial_contact.html')
        data = {'email': self.data.get('email'), 'msg': "Fomulario de contacto inicial", 
                "form_url": URL + '/forms?id=' + str(form.pk), "business_name": self.data.get('business_name')}
        notify.send_email(email_destinity=self.data.get('email'), data=data)
    
    def validation(self):
        if Forms.objects.filter(email=self.data["email"]).exists():
            raise ValueError("El correo electronico ya esta registrado")
    class ValidationError(Exception):
        pass
