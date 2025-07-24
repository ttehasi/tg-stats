from django.shortcuts import render
from django.views.generic.base import View
import inertia


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html'
        )
        
    
class ListView(View):
    def get(self, request, *args, **kwargs):
        data = [1, 2, 3, 4, 5]
        return inertia.render(
            request,
            'List',
            {'data': data}
        )