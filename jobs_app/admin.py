from django.contrib import admin
from jobs_app.models import job,platform,company_review

# Register your models here.
admin.site.register(job)
admin.site.register(platform)
admin.site.register(company_review)