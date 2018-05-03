from django.http import Http404
from django.shortcuts import render, get_object_or_404
from bank.models import Account
	
class AccountView(APIView):
	def get(self, request):
		accounts = Account.objects.all()
		serialized_account = AccountSerializer(
			data=accounts, many=True)
		return JSONResponse(serialized_account.data)
	
	def post(self, request):
		data = JSONParser().parse(request)
		serializer = AccountSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
			

def account_handler(request, id=None):
	if request.method == 'POST':
		new_account = Account(
			name=request.POST.get('name'),
			type=request.POST.get('type')
		)
		new_account.save()
		context = { 'new_account': new_account }
		return render(request, 'bank/new_account.html', context)
# Create your views here.
