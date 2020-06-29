# generic views for all modules.
def handler404(request, exception=None):
	return render(request, '404.html', status=404)


def handler500(request, exception=None):

	return render(request, '500.html', status=500)
