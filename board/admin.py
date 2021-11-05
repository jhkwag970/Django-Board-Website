from django.contrib import admin

from board.models import Reply, Board

# Register your models here.
admin.site.register(Board)
admin.site.register(Reply)
