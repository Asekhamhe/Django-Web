from django.contrib import admin
# Import your model
from collection.models import Profile

# Set up automated slug creation
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    # We want this to display on the admin dashboard
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
admin.site.register(Profile, ProfileAdmin)
