from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import NotFound
from hackaton.apps.business.models import Company, Unions
from django.db import transaction
 
class CompanyRepository:
    
    def retrieve(self, company_id):
        instance = get_object_or_404(Company, id=company_id)
        return instance
    
    def retrieve_company_by_form(self, form_id):
        company_instance = Company.objects.filter(form_id=form_id, parent__isnull=False).first()
        if company_instance is None:
            raise NotFound("Not found.")
        return company_instance
 
 
class UnionsRepository:
    
    def retrieve(self, union_id):
        """
        """
        instance = get_object_or_404(Unions, id=union_id)
        return instance

    def unions_list_company(self, company: Company):
        """
        """
        unions = Unions.objects.filter(company=company)
        return unions
    
    def list(self):
        return Unions.objects.all()
    
    def create_unions(self, unions, company):
        
        with transaction.atomic():
            for union in unions:
                union.update({"company": company})
                try:
                    Unions.objects.create(**union)
                except Exception as e:
                    print(e)
                    raise ValueError("Error al guaradar un sindicato")