class ListUnionsCase:
    
    def __init__(self, repository, company_repository):
        self.repository = repository
        self.company_repository = company_repository
    
    def execute(self, form_id):
        company = self.company_repository.retrieve_company_by_form(form_id)
        return self.repository.unions_list_company(company)


class CreateUnionsCase:
    
    def __init__(self, repository, company_repository):
        self.repository = repository
        self.company_repository = company_repository
    
    def set_params(self, data):
        self.data = data
    
    def execute(self):
        company = self.company_repository.retrieve_company_by_form(self.data.get('form_id'))
        self.repository.create_unions(self.data.get('unions'), company)
    
    def validation(self):
        pass
        
    class ValidationError(Exception):
        pass