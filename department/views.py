from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from .form import ComputerForm
from django.views.decorators.csrf import csrf_exempt
from models import Computer

# Create your views here.

@csrf_exempt
def home(request):
	print "User try to login: home "
	print("Credential :    %s             %s   "%(request.GET.get('username'), request.GET.get('password')))

	computers = Computer.objects.all()
	
	for computer in computers:	
		#print "Id : %d" % (int(computer.id))
		print "Name : " + computer.name
		#print "Designation : " + computer.designation
	return render_to_response("index.html", {"computers":computers})
	
@csrf_exempt
def department(request):
	print "------------------------------------------------------"
	print "User try to login: department "
	print("Credential :    %s             %s   "%(request.GET.get('username'), request.GET.get('password')))

	print "=============Current computer============= "
	print "ID : %s        Name  	 %s        Designation : %s  Profile : %s   Salary : %s      Address  :  %s "\
	 % (request.GET.get('id'), request.GET.get('name'), request.GET.get('designation'), \
	request.GET.get('profile'), request.GET.get('salary'), request.GET.get('address'))
	
	name_val =  request.GET.get('name')
	desig_val = request.GET.get('designation')
	profile_val = request.GET.get('profile')
	salary_val = request.GET.get('salary')
	address_val= request.GET.get('address')

	# check for null values
	if name_val != '' and name_val != None and desig_val != '' and desig_val != None \
	 and profile_val != ''  and profile_val != None and salary_val != '' \
	and salary_val is not  None and address_val is not '' and address_val is not None:
	# make a object of model
		comp = Computer(name= name_val, designation=desig_val, work_profile=profile_val,\
	 	salary=salary_val, address=address_val)
		comp.save()
		print "saving values"
	else:
		print("Please enter all values..")
	
	return render_to_response("next.html")
	
def staff(request):
	print "showing staff"
	return render_to_response("staff.html")

def projects(request):
	print "showing projects "
	return render_to_response("projects.html")

def rev_exp(request):
	print("Showing revenue expenses")
	return render_to_response("revANDexp.html")


def workhours(request):
	print("Showing hours management")
	return render_to_response("workhours.html")

def carrier(request):
	print("carrier management")
	return render_to_response("carrier.html")

def about_us(request):
	print("carrier about us")
	return render_to_response("about.html")

def sign_up(request):
	print("carrier about us")
	return render_to_response("signin.html")

def userlogin(request):
	print("login")
	return render_to_response("userlogin.html")
