from .models import Trieda
from .models import Student
from .models import Ucitel
from .models import Hodina
from .models import Predmet
from django.contrib import admin

admin.site.register(Trieda)
admin.site.register(Student)
admin.site.register(Ucitel)
admin.site.register(Hodina)
admin.site.register(Predmet)

