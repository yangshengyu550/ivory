#import django_tables2 as tables
#from .models import Doubanmovie
#class Showlist(tables.Table):
    class Meta:
        model = Doubanmovie
        template_name = 'django_tables2/bootstrap.html'