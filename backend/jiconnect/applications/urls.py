from .models import Customer, Application, Employee, Appliances
from django.urls import path
from .views import CustomerListView, CustomerView, CustomerUpdateView
from .views import EmployeeListView, EmployeeView, EmployeeUpdateView
from .views import ApplicationListView, AppliancesListView, ApplicationView, ApplicationPostView, ApplicationDeleteView, ApplicationUpdateView, ApplicationDataListView, ApplicationAnalyticsListView, ApplicationGraphsListView, ApplicationAllListView, CustomerClerkView, ApplicationDesignerListView, ApplicationEngineerListView, ApplicationFilterListView

# api format to be domain/api/appname/urlpathinapp 
urlpatterns = [

    # Customer
    path('customers/', CustomerListView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('customer/<pk>', CustomerClerkView.as_view()),
    path('customer/update/', CustomerUpdateView.as_view()),

    # Employee
    path('employees/', EmployeeListView.as_view()),
    path('employee/<pk>', EmployeeView.as_view()),
    path('employee/update/<pk>', EmployeeUpdateView.as_view()),

    # Application
    path('applications/', ApplicationListView.as_view()),
    path('appliances/', AppliancesListView.as_view()),
    path('applications/<pk>', ApplicationView.as_view()),
    path('applications/upload/', ApplicationPostView.as_view()),
    path('applications/delete/<pk>', ApplicationDeleteView.as_view()),
    path('applications/update/<pk>', ApplicationUpdateView.as_view()),
    path('applications/filter/<str:filterstatus>', ApplicationFilterListView.as_view()),
    path('applications/analytics/', ApplicationAnalyticsListView.as_view()),
    path('applications/graphs/', ApplicationGraphsListView.as_view()),

    # Employees Requests
    path('applications/data/', ApplicationDataListView.as_view()),
    path('applications/all/', ApplicationAllListView.as_view()),


    # Designer requests
    path('applications/designer/', ApplicationDesignerListView.as_view()),

    # Engineer requests
    path('applications/engineer/', ApplicationEngineerListView.as_view()),
]