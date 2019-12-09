from django.contrib import admin
from .models import FormalShirt,CasualShirt,Jeans,Shorts,FormalShirt_W,CasualShirt_W,Jeans_W,Shorts_W
# Register your models here.
class FormalShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')


admin.site.register(FormalShirt,FormalShirtAdmin)

class CasualShirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')

admin.site.register(CasualShirt,CasualShirtAdmin)

class JeansAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')

admin.site.register(Jeans,JeansAdmin)


class ShortsAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')

admin.site.register(Shorts,ShortsAdmin)

class FormalShirt_WAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')


admin.site.register(FormalShirt_W,FormalShirt_WAdmin)

class CasualShirt_WAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')

admin.site.register(CasualShirt_W,CasualShirt_WAdmin)

class Jeans_WAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')

admin.site.register(Jeans_W,Jeans_WAdmin)


class Shorts_WAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','availabel','created','updated')
admin.site.register(Shorts_W,Shorts_WAdmin)
