from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView


from .models import *
# from .parser import all

def index(request):
    currency = all
    news = News.objects.order_by("-created_at")[:3]
    slides = Slides.objects.order_by(("-date"))[:5]
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html', locals())


def prices(request):
    rates = Rates.objects.latest('date')
    return render(request, 'prices.html', locals())


def price_detail(request, pk):
    rates = Rates.objects.filter(pk=pk).first()
    return render(request, 'price_details.html', locals())

def all_prices(request):
    rates = Rates.objects.all()
    return render(request, 'all_prices.html', locals())


def testimonials(request):
    t = Testimonials.objects.all()
    return render(request, 'testimonials.html', locals())


def plans(request):
    plans = Plans.objects.all()
    progress = Progress.objects.all()
    return render(request, 'plans.html', locals())


def plan_detail(request, pk):
    plans = Plans.objects.filter(pk=pk).first()
    return render(request, 'plan-details.html', locals())


def progress_detail(request, pk):
    progress = Progress.objects.filter(pk=pk).first()
    return render(request, 'progress_details.html', locals())

def partners(request):
    tables = Tables.objects.all()
    return render(request, 'partners.html', locals())


def ecology(request):
    return render(request, 'ecology.html', locals())


def news_detail(request, pk):
    post = News.objects.filter(pk=pk).first()
    return render(request, 'news_detail.html', locals())


def all_news(request):
    news = News.objects.all()
    return render(request, 'news_list.html', locals())


def all_leaders(request):
    leaders = Leaders.objects.all()
    return render(request, 'all_leaders.html', locals())


def leader_detail(request, pk):
    leader = Leaders.objects.filter(pk=pk).first()
    return render(request, 'leader_detail.html', locals())


# def tables(request, pk):
#     table = Tables.objects.filter(pk=pk).first()
#     return render(request, 'table_detail.html', locals())

# class TableView(TemplateView):
#     template_name = 'table_detail.html'


#     def get_context_data(self, pk, **kwargs):
#         table = Tables.objects.filter(pk=pk).first()
#         ctx = super(TableView, self).get_context_data(**kwargs)
#         ctx['counter'] = [1, 2, 3, 4, 5]
#         ctx['table'] = table
#         ctx['header'] = ['№', 'Наименование параметров', 'Нормы для нефти', 'Метод испытания', 'Примечание']
#         ctx['rows'] = [
#             [
#                 {'id': 1, 'name': 'Плотность, кг/м3 при температуре 20° С, не более', 'norms': '895,0', 'method': 'ГОСТ 3900', 'note': ''},
#                 {'id': 2,  'name': 'Массовая доля воды, % не более', 'norms': '1,0', 'method': 'ГОСТ 2477', 'note': ''},
#                 {'id': 3,  'name': 'Массовая концентрация хлористых солей, мг/дм3 не более', 'norms': '300', 'method': 'ГОСТ 21534', 'note': ''},
#                 {'id': 4,  'name': 'Массовая доля механических примесей, % не более', 'norms': '0,05', 'method': 'ГОСТ 6370', 'note': ''},
#                 {'id': 5,  'name': 'Давления насыщенных паров, кПа (мм РТ, ст), не более', 'norms': '66,7 (500)', 'method': 'ГОСТ 1756', 'note': ''},
#                 {'id': 6,  'name': 'Массовая доля парафина, % не более', 'norms': '6,0', 'method': 'ГОСТ 11851', 'note': '(0-10%)'},
#                 {'id': 7,  'name': 'Массовая доля сероводорода, млн-1 (ppm), не более', 'norms': '50', 'method': 'ГОСТ Р50802', 'note': ''},
#                 {'id': 8,  'name': 'Массовая доля метил- и этил меркаптанов в сумме, млн-1 (ppm), не более', 'norms': 'отсутствие', 'method': 'ГОСТ Р 50802', 'note': ''},
#                 {'id': 9,  'name': 'Массовая доля серы, % не более', 'norms': '0,4', 'method': 'ГОСТ Р 51947', 'note': 'Макс 0,6%'},
#                 {'id': 10,  'name': 'Массовая доля серы, % не более 150° C/ 350° C', 'norms': '12 / 50', 'method': 'ГОСТ 2177', 'note': 'По требованиям КПК: (10-30) / (48-68)'},
#                 {'id': 11,  'name': 'Температура застывания,  °С не выше', 'norms': 'Плюс 10', 'method': 'ГОСТ 20287', 'note': '(-5 +15)'},
#             ],
#             [
#                 {'id': 1,  'name': 'Плотность, кг/м3 при температуре 20° С, не более', 'norms': '830,0', 'method': 'ГОСТ 3900', 'note': ''},
#                 {'id': 2,  'name': 'Массовая доля воды, % не более', 'norms': '0,5', 'method': 'ГОСТ 2477', 'note': '(0-1)'},
#                 {'id': 3,  'name': 'Фракционный состав: 10% перегоняется при температуре, °С, не ниже / 98% перегоняется при температуре, °С, не выше', 'norms': '150 / 310', 'method': 'ГОСТ 2177', 'note': ''},
#                 {'id': 4,  'name': 'Температура вспышки в закрытом тигле, °С, не ниже', 'norms': '40', 'method': 'ГОСТ 6356', 'note': ''},
#                 {'id': 5,  'name': 'Температура помутнения, °С, не выше', 'norms': 'минус 10', 'method': 'ГОСТ 5066', 'note': ''},
#                 {'id': 6,  'name': 'Кислотность, мг КОН на 100см3 топлива, не более', 'norms': '1,5', 'method': 'ГОСТ 5985', 'note': ''},
#                 {'id': 7,  'name': 'Зольность, % не более', 'norms': '0,005', 'method': 'ГОСТ 1461', 'note': ''},
#                 {'id': 8,  'name': 'Массовая доля серы, % не более', 'norms': '0,1', 'method': 'ГОСТ Р 51947 / ГОСТ 19121', 'note': ''},
#                 {'id': 9,  'name': 'Концентрация фактических смол, мг/100см3 керосина не более', 'norms': '35', 'method': 'ГОСТ 8489', 'note': ''},
#             ],
#             [
#                 {'id': 1,  'name': 'Плотность, кг/м3 при температуре 20° С, не более', 'norms': 'Не нормируется', 'method': 'ГОСТ 3900', 'note': ''},
#                 {'id': 2,  'name': 'Массовая доля воды, % не более', 'norms': '0,5', 'method': 'ГОСТ 2477', 'note': ''},
#                 {'id': 3,  'name': 'Фракционный состав: 10% перегоняется при температуре, °С, не ниже / 98% перегоняется при температуре, °С, не выше', 'norms': '150 / 360', 'method': 'ГОСТ 2177', 'note': ''},
#                 {'id': 4,  'name': 'Температура вспышки в закрытом тигле, °С, не ниже', 'norms': '45', 'method': 'ГОСТ 6356', 'note': ''},
#                 {'id': 5,  'name': 'Температура помутнения, °С, не выше', 'norms': 'минус 5', 'method': 'ГОСТ 5066', 'note': ''},
#                 {'id': 6,  'name': 'Кислотность, мг КОН на 100см3 топлива, не более', 'norms': '4,0', 'method': 'ГОСТ 5985', 'note': ''},
#                 {'id': 7,  'name': 'Массовая доля серы, % не более', 'norms': '0,3', 'method': 'ГОСТ Р 51947', 'note': ''},
#                 {'id': 8,  'name': 'Йодное число, г йода на 100г топлива не более', 'norms': '5,0', 'method': 'ГОСТ 2070', 'note': ''},
#             ],
#             [
#                 {'id': 1,  'name': 'Плотность, кг/м3 при температуре 20° С, не более', 'norms': 'Не нормируется', 'method': 'ГОСТ 3900', 'note': ''},
#                 {'id': 2,  'name': 'Массовая доля воды, % не более', 'norms': '0,5', 'method': 'ГОСТ 2477', 'note': ''},
#                 {'id': 3,  'name': 'Фракционный состав: 10% перегоняется при температуре, °С, не ниже / 90% перегоняется при температуре, °С, не выше', 'norms': '100 / 350 и выше', 'method': 'ГОСТ 2177', 'note': ''},
#                 {'id': 4,  'name': 'Содержание сероводорода', 'norms': 'Отсутствует', 'method': 'ГОСТ 17323', 'note': ''},
#                 {'id': 5,  'name': 'Содержание механических примесей', 'norms': 'Отсутствует', 'method': 'ГОСТ 6370', 'note': ''},
#                 {'id': 6,  'name': 'Массовая доля серы, %, не более', 'norms': '0,25', 'method': 'ГОСТ Р 51947', 'note': ''},
#                 {'id': 7,  'name': 'Испытание на медной пластине', 'norms': 'выдерживает', 'method': 'ГОСТ 6321', 'note': ''},
#             ],
#             [
#                 {'id': 1,  'name': 'Плотность, кг/м3 при температуре 20° С, не более', 'norms': 'Не нормируется', 'method': 'ГОСТ 3900', 'note': ''},
#                 {'id': 2,  'name': 'Массовая доля воды, % не более', 'norms': '0,5', 'method': 'ГОСТ 2477', 'note': ''},
#                 {'id': 3,  'name': 'Фракционный состав: 50% перегоняется при температуре, °С не более / Конец кипения, °С, не выше', 'norms': '280 / 360', 'method': 'ГОСТ 2177', 'note': ''},
#                 {'id': 4,  'name': 'Содержание сероводорода', 'norms': 'Отсутствует', 'method': 'ГОСТ 17323', 'note': ''},
#                 {'id': 5,  'name': 'Содержание механических примесей', 'norms': 'Отсутствует', 'method': 'ГОСТ 6370', 'note': ''},
#                 {'id': 6,  'name': 'Температура определяемая вспышки в закрытом тигле, °С, не ниже', 'norms': '60', 'method': 'ГОСТ 6356', 'note': ''},
#                 {'id': 7,  'name': 'Массовая доля серы, %, не более', 'norms': '0,25', 'method': 'ГОСТ Р 51947', 'note': ''},
#             ]

#         ]
#         return ctx


