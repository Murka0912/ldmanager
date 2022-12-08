from django.urls import path
import pythoncom
from . import views
pythoncom.CoInitialize()

urlpatterns = [
    path('',views.index, name= 'addsrv'),
    path('home/', views.srv, name='srv'),
    path('listsrv', views.listsrv, name='listsrv'),
    path('db', views.listdb, name='listdb'),
    path('<int:pk>', views.SubdDetailView.as_view(),name='subd-detail'),
    path('res/', views.result, name='result'),
    path('download', views.download, name='download'),
    path('res/node/<slug:cat_slug>/',views.resultList.as_view(), name='res'),
    path('details/<int:id_srv>',views.monDetail, name='res-detail'),
    path('newres', views.dashboard, name='srvform'),
    path('dbname/', views.dbname, name='dbname'),
    path('que', views.query, name='que'),
    path('services', views.services, name='services'),
    path('manageserv', views.manage_service, name='manageservices'),
    path('export/<slug:slug>/<str:name>', views.exportDataxls, name='export'),
    path('settings', views.settings, name='settings'),
    path('logs', views.applog, name='logs'),
    path('synth',views.synth, name='synthec'),
    path('show_result_task', views.show_result_task, name='show1'),
    path('call_proc', views.get_logs_func, name='call_proc'),
    path('medo',views.medo, name='medo')


]