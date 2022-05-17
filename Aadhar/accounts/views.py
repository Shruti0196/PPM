from ast import Add
from msilib import add_data
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .models import *
# from django.conf import settings
# # User = settings.AUTH_USER_MODEL
from .serializers import UserSerializer,AddressSerializer,QualificationSerializer,BankSerializer,personaldetailsSerializer,PastJobExpSerializer,AadharSerializer
# # Create your views here.
# @csrf_exempt
 # @method_decorator(csrf_protect)
# @api_view(['POST'])
# def registeruser(self,request,*args,**kwargs):
class RegisterUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid'})
        group=Group.objects.get(name='Manager')
                    
        userr=serializer.save()
        userr.groups.add(group)
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ =Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'valid'})
    def get(self,request):    
        serializer=UserSerializer()
        return render(request,'signup.html',{'serializer':serializer})


@api_view(['POST'])
def userlogin(request):
    serializer=UserSerializer(request.data)
    username=serializer.data['username']
    password=serializer.data['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
            login(request,user)
            return Response('logged in')

class StaffUser(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid'})
        group=Group.objects.get(name='Staff')
                    
        userr=serializer.save()
        userr.groups.add(group)
        user = User.objects.get(username=serializer.data['username'])
        token_obj, _ =Token.objects.get_or_create(user=user)

        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'valid'})

# @api_view(['POST'])
# def stafflogin(request):
#     serializer=UserSerializer(request.data)
#     username=serializer.data['username']
#     password=serializer.data['password']
#     user = authenticate(request,username=username,password=password)
#     if user is not None:
#             login(request,user)
#             return Response('logged in')    

# @login_required(login_url='login')
from .decorators import unauthenticated_user,allowed_users

#Aadhar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listAadhar(request):
        
        aadhar=Aadhar.objects.all()
        serializer=AadharSerializer(aadhar,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createAadhar(request):
        try:
            serializer=AadharSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Addresss Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateAadhar(request, pk):
    try:
        model = Aadhar.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = AadharSerializer(model,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteAadhar(request, pk):
    item = Aadhar.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")

#address

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listaddress(request):
        
        address=Address.objects.all()
        serializer=AddressSerializer(address,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createaddress(request):
        try:
            serializer=AddressSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Addresss Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateaddress(request, pk):
    try:
        model = Address.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = AddressSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteaddress(request, pk):
    item = Address.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")

#qualification

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listqualification(request):
        qualification=Qualification.objects.all()
        serializer=QualificationSerializer(qualification,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createqualification(request):
        try:
            serializer=QualificationSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updatequalification(request, pk):
    try:
        model = Qualification.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = QualificationSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletequalification(request, pk):
    item = Qualification.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")   

#bank 

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listbank(request):
        bank=Bank.objects.all()
        serializer=BankSerializer(bank,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createbank(request):
        try:
            serializer=BankSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updatebank(request, pk):
    try:
        model = Bank.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = BankSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletebank(request, pk):
    item = Bank.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")   

#personaldetails

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listpersonaldetails(request):
        details=PersonalDetails.objects.all()
        serializer=personaldetailsSerializer(details,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createpersonaldetails(request):
        try:
            serializer=personaldetailsSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updatepersonaldetails(request, pk):
    try:
        model = PersonalDetails.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = personaldetailsSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletepersonaldetails(request, pk):
    item = PersonalDetails.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")   

#pastjobexp

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def listpastjobexp(request):
        pastjobexp=PastJobExp.objects.all()
        serializer=PastJobExpSerializer(pastjobexp,many=True,context={"request":request})
        response_dict={"data":serializer.data}
        return Response(response_dict)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def createpastjobexp(request):
        try:
            serializer=PastJobExpSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Data Saved Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving  Data"}
        return Response(dict_response)


@api_view(['GET','PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updatepastjobexp(request, pk):
    try:
        model = PastJobExp.objects.get(pk=pk)
    except:
        return Response('Not Found')
    if request.method == 'PUT':
        serializer = PastJobExpSerializer(model, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("Updated")
        else:
            return Response ("Failed")

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deletepastjobexp(request, pk):
    item = PastJobExp.objects.get(pk=pk)
    item.delete()
    return Response("Deleted")   

#get details acc to aadhar number

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharaddress(request,pk):
        details=Aadhar.objects.get(pk=pk)
        add_data=Address.objects.filter(id=details.address.get().id) 
        serializer=AddressSerializer(add_data,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharqualification(request,pk):
        details=Aadhar.objects.get(pk=pk)
        add_data=Qualification.objects.filter(id=details.qualification.id) 
        serializer=QualificationSerializer(add_data,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharbank(request,pk):
        details=Aadhar.objects.get(pk=pk)
        add_data=Bank.objects.filter(id=details.bank.id) 
        serializer=BankSerializer(add_data,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharprsnldetails(request,pk):
        details=Aadhar.objects.get(pk=pk)
        add_data=PersonalDetails.objects.filter(id=details.prsnl_details.id) 
        serializer=personaldetailsSerializer(add_data,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharpastjobexp(request,pk):
        details=Aadhar.objects.get(pk=pk)
        add_data=PastJobExp.objects.filter(id=details.past_job_exp.id) 
        serializer=PastJobExpSerializer(add_data,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadhardata(request,pk):
        details=Aadhar.objects.get(pk=pk)
        serializer=AadharSerializer(details,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharactive(request):
        details=Aadhar.objects.filter(Is_active=True)
        serializer=AadharSerializer(details,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def aadharinactive(request):
        details=Aadhar.objects.filter(Is_active=False)
        serializer=AadharSerializer(details,many=True,context={"request":request}) 
        response_dict={"data":serializer.data}
        return Response(response_dict)  

        # return Response('got')
# print(details.address.all())
        # print(details.address.get().id)
        # # serializer=[]
        # # for i in details.address.all():
        # #    id=i.get().id
        # # add_data=Address.objects.filter(id=(details['address']))
        # serializer=AddressSerializer(add_data,many=True,context={"request":request})
# from django.contrib import messages



# # @allowed_users(allowed_roles=['Admin'])
# def homepage(request):
#     return render(request, 'homepage.html')
# # def showform(request):
# #     form=TodoForm()
# #     return render(request,'index.html',{'form':form})
# # from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView

# from .forms import UserCreationForm
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView

# def homepage(request):
#     return render(request, 'homepage.html')

# # @csrf_exempt
# @unauthenticated_user
# def staffsignup(request):
#     if request.method == 'POST':
#             form=UserCreationForm(request.POST)
#             if form.is_valid():
#                 user=form.save()
#                 # username=form.cleaned_data.get('username')
#                 group=Group.objects.get(name='staff')
#                 user.groups.add(group)
#                 # messages.success(request,'Account was created for '+username)
#                 return redirect("stafflogin")
#     if request.method == 'GET':
#         form=UserCreationForm()
#         return render(request,'signup.html',{'form':form})

# # @unauthenticated_user
# # def managersignup(request):
# #         form=MyUserCreationForm()
# #         if request.method =='POST':
# #             form=MyUserCreationForm(request.POST)
# #             if form.is_valid():
# #                 user=form.save()
# #                 username=form.cleaned_data.get('username')
# #                 group=Group.objects.get(name='Manager')
# #                 user.groups.add(group)
# #                 # messages.success(request,'Account was created for '+username)
# #                 return redirect("managerlogin")
# #         return render(request,'signup.html',{'form':form})

# # @csrf_exempt
# @unauthenticated_user
# def stafflogin(request):
#     if request.method == 'POST':
#             email = request.POST.get('email')
#             password = request.POST.get('password')
#             user = authenticate(request,email=email,password=password)
#             # if auth.authenticate(username=username, password=password):
#             if user is not None:
#                 login(request,user)
#                 return redirect('/')
#             return redirect('stafflogin')

#     if request.method == 'GET':
#             return render(request, 'login.html')
#             # return HttpResponse('Login')+

# # @unauthenticated_user
# # def managerlogin(request):
    
# #         if request.method == 'POST':
# #             username = request.POST.get('username')
# #             password = request.POST.get('password')
# #             user = authenticate(request,username=username,password=password)
# #             # if auth.authenticate(username=username, password=password):
# #             if user is not None:
# #                 login(request,user)
# #                 return redirect('addform')
# #             return redirect('userlogin')

# #         if request.method == 'GET':
# #             return render(request, 'login.html')

# # def userlogout(request):
# #     logout(request)
# #     return redirect('/')

# # @login_required(login_url='login')
# # def addform(request):
# #     form=TodoForm()
# #     if request.method=='POST':
# #         # print("Post:",request.POST)
# #         form=TodoForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('/details')
# #     if request.method=='GET':        
# #         return render(request,'index.html',{'form':form}) 

# # @login_required(login_url='login')
# # @allowed_users(allowed_roles=['Admin'])
# # def adddetailsform(request):
# #     form=DetailsForm()
# #     if request.method=='POST':
# #         form=DetailsForm(request.POST)
# #         if form.is_valid():
# #             form.save()
            
# #             return redirect('addform')
# #     return render(request,'index.html',{'form':form})

# # @login_required(login_url='login')

# # def updateworkdetails(request,Work1):
# #     # work=WorkDetails.objects.get(Q(WorkDetails__Work__Work=pk))
# #     # work=WorkDetails.objects.filter(Work=work1)
# #     # print(work)
# #     work=WorkDetails.objects.get(Work=Work1)
# #     print(work)
# #     form=DetailsForm(instance=work)
# #     if request.method=='POST':
# #         form=DetailsForm(request.POST,instance=work)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('/display')
# #     return render(request,'index.html',{'form':form})

# # @login_required(login_url='login')
# # def Display(request):
# #     Todo=WorkDetails.objects.all()
# #     return render(request,'Display.html',{'Todo':Todo})

# # @login_required(login_url='login')
# # def deletework(request,pk):
# #         work=WorkDetails.objects.get(desc=pk)
# #         work.delete()
# #         return redirect('/display')

# # accounts/views.py


     

