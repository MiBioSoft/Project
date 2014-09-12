from django.contrib import admin
from django.db import models
from databasemodels.forms import UserForm, ProtocolForm
# Register your models here.

from databasemodels.models import User, Protocol, Comment, UserDescription



class CommentInline(admin.TabularInline):
    # TODO: make this work. currently same as tutorial
    model = Comment
    extra = 1 # should be expression for number of comments on the protocol

##class ProtocolAdmin(admin.ModelAdmin):
##    fieldsets = [
##        (None,              {'fields': ['title', 'description']}),
##        #('Description',     {'fields': ['description']}),
##        (None,              {'fields': ['publisher', 'pub_date']}),
##        ('Keywords',        {'fields': ['keywords']}),
##        ('Protocol',        {'fields': ['text']}),
##    ]
##    inlines = [CommentInline]
##    list_display = ['title', 'description', 'publisher', 'pub_date'] #TODO: rating too
##    search_fields = ['title'] #TODO: keywords too
##    

##class ProtocolAdmin(admin.ModelAdmin):
##    form = ProtocolForm
####
##    exclude = ['publisher']
##    list_display = ['title', 'description','text', 'publisher']
##    def save_model(self, request, obj, form, change):
##        if not obj.publisher.id:
##            obj.publisher = request.user
##        obj.save()
##    
##    
##    #gives keywords is multi to multi, unsupported
##    fieldsets = ((
##        None, {
##            'fields': ('title', 'description', 'keywords', 'text')
##            }), )
##    
##    def save_model(self, request, obj, form, change):
##        if not obj.publisher.id:
##            obj.publisher = request.user
##        
##        obj.save()
        
##class ProtocolAdmin(admin.ModelAdmin):
##    form = ProtocolForm
##    def formfield_for_foreignkey(self, db_field, request, **kwargs):
##        if db_field.name == 'publisher':
##            kwargs['initial'] = request.user.id
##        return super(ProtocolAdmin, self).formfield_for_foreignkey(
##            db_field, request, **kwargs)
##            

##    def get_some_value(self):
##        return ", ".join([x.__str__() for x in self.keywords.all()])
##        list_display(get_some_value)
##        get_some_value.short_description = 'Keywords'
admin.site.register(UserDescription)
admin.site.register(Protocol)
#admin.site.register(Protocol, ProtocolAdmin)
