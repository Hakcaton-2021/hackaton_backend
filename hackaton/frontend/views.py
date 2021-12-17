from django.shortcuts import render

from hackaton.apps.business.models import Company, CompanyType, Gratification, PaymentMobilization
from hackaton.apps.central.models import Bank, CompensationBox, Mutual
from hackaton.apps.locations.models import Comuna


class View(object):
    """ Clase de vista principal
    """

    def forms(self, key="forms"):
        country_code_active = "CL"
        response = {'active': key}
        template = 'forms.html'
        context = {"company": Company.objects.all(),
                   "type": CompanyType.objects.all(),
                   "comuna": Comuna.objects.filter(
                       country__code=country_code_active).order_by("name").all(),
                   "compensation_box": CompensationBox.objects.filter(
                       country__code=country_code_active).order_by("name").all(),
                   "mutual": Mutual.objects.filter(
                       country__code=country_code_active).order_by("name").all(),
                   "bank": Bank.objects.filter(
                       country__code=country_code_active).order_by("name").all(),
                   "gratification": Gratification.objects.all(),
                   "payment_mobilization": PaymentMobilization.objects.all(),
                   }
        response.update({'context': context})
        return render(self, template, response)
