from django.db import connections
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from .models import Application, Customer, Employee, Appliances
from .serializers import ApplicationSerializer, CustomerSerializer, EmployeeSerializer, AppliancesSerializer
from rest_framework.response import Response
from . import Data
from . import Analytics
import json

# Applications
class ApplicationListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        return Application.objects.filter(customer_id=user.id)


class AppliancesListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Appliances.objects.all()
    serializer_class = AppliancesSerializer
    pagination_class = None


class ApplicationAnalyticsListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get(self, request, format=None):
        queryset = Application.objects.all()

        total_applications = queryset.count()
        installed = Analytics.getInstalled(queryset)
        sites_visited = Analytics.getSiteVisited(queryset)
        try:
            return Response({'total_applications': total_applications, 'installed':installed, 'sites_visited': sites_visited})
        except:
            return Response({'error': 'Message failed to send'})


class ApplicationGraphsListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = None




    def get(self, request, format=None):
        queryset = Customer.objects.all()

        customers = queryset
        application_continuencies = Analytics.getApplicationconst()
        application_types = Analytics.getApplicationtypes(customers)
        application_appliance = Analytics.getApplicationAppliances(Appliances.objects.all())

        graphs = Analytics.Merge(application_continuencies, application_types, application_appliance)
        print(graphs)
        try:
            return Response(graphs)
        except:
            return Response({'error': 'Message failed to send'})




class ApplicationFilterListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get_queryset(self):
        filter_status = str(self.kwargs['filterstatus']).replace('_', ' ')
        return Application.objects.filter(app_status=str(filter_status))

class ApplicationView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer



class ApplicationPostView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ApplicationSerializer

    def post(self, request, format=None):
        data = self.request.data
        user = self.request.user
        customer = Customer.objects.get(id=user.id)


        try:
            application = Application(customer=customer, app_type=data['app_type'], plan=data['plan'], location=data['location'], app_status=data['app_status'], ref_number=data['ref_number'], site_info=data['site_info'], agree_supply=data['agree_supply'], agree_wayleave=data['agree_wayleave'], qoutation=data['qoutation'], appcontrol=data['appcontrol'], install_note=data['install_note'], proposal=data['proposal'], maplatlon=data['maplatlon'], payment=data['payment'], numapps=data['numapps'])

            application.save()
            userapp = Application.objects.get(id=application.id)
            appliances = data['allappliances']
            for i in appliances:
                appliance = Appliances(application=userapp, appliance=i['appliance'], consumption=i['consumption'], qty=i['qty'], total=i['total'])
                appliance.save()
            return Response({'success': 'Message sent successfully'})

        except:
            return Response({'error': 'Message failed to send'})



class ApplicationDeleteView(DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationUpdateView(UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer









# Employees Data
class ApplicationDataListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get(self, request, format=None):
        queryset = Application.objects.all()

        total_applications = queryset.count()
        waiting_for_qoute = Data.getWaitingForQoute(queryset)
        waiting_for_send = Data.getWaitingForSend(queryset)
        on_design = Data.getOnDesign(queryset)
        installed = Data.getInstalled(queryset)
        sites_visited = Data.getSiteVisited(queryset)
        payment_settled = Data.getPaymentSettled(queryset)

        try:
            return Response({'total_applications': total_applications, 'waiting_for_qoute': waiting_for_qoute, 'waiting_for_send': waiting_for_send, 'on_design':on_design, 'installed':installed, 'sites_visited': sites_visited, 'payment_settled':payment_settled})
        except:
            return Response({'error': 'Message failed to send'})

class ApplicationAllListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get_queryset(self):
        return Application.objects.filter(app_status="Under Review")


class ApplicationDesignerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Application.objects.all()
        query1 = queryset.filter(app_status="On Design")
        return query1

class ApplicationEngineerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    pagination_class = None

    def get_queryset(self):
        queryset = Application.objects.all()
        query1 = queryset.filter(app_status="Payment Settled")
        return query1





# Customer
class CustomerListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = None


class CustomerView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, ) # user AllowAny if its public view and no permission if its private
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, format=None):
        data = self.request.data
        user = self.request.user
        queryset = Customer.objects.get(id=user.id)


        try:
            return Response({'name': queryset.name, 'phone': queryset.phone, 'email': queryset.email, 'middle_name': queryset.middle_name, 'last_name': queryset.last_name, 'id_type': queryset.id_type, 'id_number': queryset.id_number, 'pin': queryset.pin, 'county': queryset.county, 'po_box': queryset.po_box, 'town': queryset.town, 'constituency': queryset.constituency, 'ward': queryset.ward, 'lr_number': queryset.lr_number, 'estate_village': queryset.estate_village, 'area_code': queryset.area_code, 'ccp': queryset.ccp, 'voltage': queryset.voltage, 'connect_type': queryset.connect_type, 'amd': queryset.amd, 'id_document': queryset.id_document, 'pin_certificate': queryset.pin_certificate, 'title_deed': queryset.title_deed, 'wiring_certificate': queryset.wiring_certificate, 'site_plan': queryset.site_plan})
        except:
            return Response({'error': 'Message failed to send'})


class CustomerClerkView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, ) # user AllowAny if its public view and no permission if its private
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateView(UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def put(self, request, format=None):
        data = self.request.data
        user = self.request.user

        try:
            Customer.objects.filter(customer_id=user.id).update(name=data['name'], phone=data['phone'], email=data['email'], middle_name=data['middle_name'], last_name=data['last_name'], id_type=data['id_type'], id_number=data['id_number'], pin=data['pin'], county=data['county'], po_box=data['po_box'], town=data['town'], constituency=data['constituency'], ward=data['ward'], lr_number=data['lr_number'], estate_village=data['estate_village'], area_code=data['area_code'], ccp=data['ccp'], voltage=data['voltage'], connect_type=data['connect_type'], amd=data['amd'], id_document=data['id_document'], pin_certificate=data['pin_certificate'], title_deed=data['title_deed'], wiring_certificate=data['wiring_certificate'], site_plan=data['site_plan'])
            return Response({'success': 'Message sent successfully'})

        except Exception as e:
            return Response({'error': 'Message failed to send'})


# Employee
class EmployeeListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = None

class EmployeeView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateView(UpdateAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer