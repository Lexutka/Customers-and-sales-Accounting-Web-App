def clientpage(request,x):
    error = ''
    if request.method == 'POST':
        form = ClientForm(request.POST.get(pk==f'http://127.0.0.1:8000/{x}'))
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ClientForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'clientpage.html', context)