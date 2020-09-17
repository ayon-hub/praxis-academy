from django.shortcuts import render,redirect
from . import models

def index(req):
    if req.POST:
        models.Pegawai.objects.create(nama=req.POST['nama'], contact=req.POST['contact'])
        return redirect('/pegawai/')

    tasks = models.Pegawai.objects.all()
    return render(req, 'pegawai/index.html', {
        'data': tasks,
    })

def detail(req, id):
    task = models.Pegawai.objects.filter(pk=id).first()
    return render(req, 'pegawai/details.html', {
        'data': task,
    })

def delete(req, id):
    models.Pegawai.objects.filter(pk=id).delete()
    return redirect('/pegawai/')
    
def update(req, id):
    if req.POST:
        task = models.Pegawai.objects.filter(pk=id).update(nama=req.POST['nama'], contact=req.POST['contact'])
        return redirect('/pegawai/')
        
    task = models.Pegawai.objects.filter(pk=id).first()
    return render(req, 'pegawai/update.html', {
        'data': task,
    })
