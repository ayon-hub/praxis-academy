from django.shortcuts import render,redirect
from . import models

def index(req):
    if req.POST:
        models.Bahan.objects.create(nama=req.POST['nama'], stok=req.POST['stok'])
        return redirect('/bahan/')

    tasks = models.Bahan.objects.all()
    return render(req, 'bahan/index.html', {
        'data': tasks,
    })

def detail(req, id):
    task = models.Bahan.objects.filter(pk=id).first()
    return render(req, 'bahan/details.html', {
        'data': task,
    })

def delete(req, id):
    models.Bahan.objects.filter(pk=id).delete()
    return redirect('/bahan/')
    
def update(req, id):
    if req.POST:
        task = models.Bahan.objects.filter(pk=id).update(nama=req.POST['nama'], stok=req.POST['stok'])
        return redirect('/bahan/')
        
    task = models.Bahan.objects.filter(pk=id).first()
    return render(req, 'bahan/update.html', {
        'data': task,
    })
