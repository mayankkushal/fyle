from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import *
# Register your models here.

class BankAdmin(ImportExportModelAdmin):
	pass


class BranchResource(resources.ModelResource):

    class Meta:
        model = Branch
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('ifsc',)

class BranchAdmin(ImportExportModelAdmin):
	resource_class = BranchResource

	def before_import(self, dataset, dry_run):
		if dataset.headers:
				dataset.headers = [str(header).lower().strip() for header in dataset.headers]
		#if you already have a id column in your file with values for this column then don't use below code
		if 'id' not in dataset.headers:
				dataset.headers.append('id')


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)