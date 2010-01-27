from django.conf.urls.defaults import *
import charts.views as views

urlpatterns = patterns('charts',
                       (r'^charts/$', 'views.show_results'),
                       (r'^get_kml/$', 'views.get_governorates')
                       )

handler404 = 'charts.views.view_404'
handler500 = 'charts.views.view_500'
