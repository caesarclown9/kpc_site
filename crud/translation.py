from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Social)
class SocialTranslationOptions(TranslationOptions):
    fields = ('title', 'body')



@register(Leaders)
class LeadersTranslationOptions(TranslationOptions):
    fields = ('firstname', 'lastname', 'midname', 'position', 'body')


@register(Tables)
class TablesTranslationOptions(TranslationOptions):
    fields = ('name',)



@register(Slides)
class SlidesTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Testimonials)
class TestimonialsTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'text')


@register(Plans)
class PlansTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Progress)
class ProgressTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

