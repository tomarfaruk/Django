from django.contrib import admin
from .models import Userprofile

# Register your models here.
class usrprofileadmin(admin.ModelAdmin):
    list_display = ('user','user_info', 'city', 'phone', 'image', 'email', 'username')

    def user_info(self, obj):
        return obj.discription
    def username(self, obj):
        return obj.user.first_name
    def email(self, obj):
        return obj.user.email

    def get_queryset(self, request):
        queryset = super(usrprofileadmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

admin.site.register(Userprofile, usrprofileadmin)
