from hackaton.apps.forms.notifications import Notifications

class  CreateFormCase:
    
    def __init__(self, repository):
        self.repository = repository
    
    def set_params(self, data):
        self.data = data
    
    def execute(self):
        self.repository.create(self.data)
        notify = Notifications(send_email=True, template='email/initial_contact.html')
        data = {'email': self.data.get('email'), 'msg': "Fomulario de contacto inicial"}
        notify.send_email(email_destinity=self.data.get('email'), data=data)
        
    class ValidationError(Exception):
        pass
