from django.contrib import admin

from .models import *

class NewsImageAdmin(admin.StackedInline):
    model = NewsImage


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin]

    class Meta:
        model = News


class SocialImageAdmin(admin.StackedInline):
    model = SocialImage


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    inlines = [SocialImageAdmin]

    class Meta:
        model = Social


class PlansImageAdmin(admin.StackedInline):
    model = PlansImage

@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    inlines = [PlansImageAdmin]

    class Meta:
        model = Plans


class ProgressImageAdmin(admin.StackedInline):
    model = ProgressImage

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    inlines = [ProgressImageAdmin]

    class Meta:
        model = Progress


admin.site.register(Rates)
admin.site.register(Tables)
admin.site.register(Leaders)
admin.site.register(Slides)
admin.site.register(Testimonials)
admin.site.register(Partners)


