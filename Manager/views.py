from django.shortcuts import render


# Render the main Page for the shopping website

def main(request):
	return render(request, 'main.html')

