from django.shortcuts import render


class View(object):
    """ Clase de vista principal
    """

    def forms(self, key="forms"):
        response = {'active': key}
        template = 'forms.html'
        context = {}
        response.update({'context': context})
        return render(self, template, response)
