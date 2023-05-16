from django.shortcuts import render,redirect
from .models import Melhores,Mortes

def home(request):
    melhores = Melhores.objects.all()
    mortes = Mortes.objects.all()
    context = {"Melhores":melhores, "Mortes":mortes}
    return render(request, "home.html", context=context)

def create_melhores(request):
    if request.method == 'POST':
        print(request.POST)
        Melhores.objects.create(
            ator=(request.POST["ator"]),
            temporada=(request.POST["temporada"]),
            personagem=(request.POST["personagem"]),
        )
        return redirect("home")
    return render(request, "melhores_form.html")

def create_mortes(request):
    if request.method == 'POST':
        print(request.POST)
        Mortes.objects.create(
            nome=(request.POST["nome"]),
            personagem=(request.POST["personagem"]),
            motivoMorte=(request.POST["motivoMorte"]),
            data=(request.POST["data"]),
        )
        return redirect("home")
    return render(request, 'mortes_form.html')

def update_melhores(request, melhores_id):
    melhores = Melhores.objects.get(id=melhores_id)

    melhores.temporada = melhores.temporada.strftime('%Y-%m-%d')
  
    if request.method == "POST":
        melhores.ator = request.POST["ator"]
        melhores.personagem = request.POST["personagem"]
        melhores.temporada = request.POST["temporada"]
        melhores.save()
        return redirect("home")

    return render(request, "melhores_form.html", context={"Melhores": melhores})


def delete_melhores(request, melhores_id):
    melhores = Melhores.objects.get(id=melhores_id)
    if request.method == "POST":
        if "confirm" in request.POST:
            melhores.delete()
            return redirect("home")

    return render(request, "delete_melhores.html", context={"Melhores": melhores})

def update_mortes(request, mortes_id):
    mortes = Mortes.objects.get(id=mortes_id)
    
    mortes.data = mortes.data.strftime('%Y-%m-%d')

    if request.method == "POST":
        mortes.nome = request.POST["nome"]
        mortes.personagem = request.POST["personagem"]
        mortes.motivoMorte = request.POST["motivoMorte"]
        mortes.data = request.POST["data"]
        mortes.save()
        return redirect("home")

    return render(request, "mortes_form.html", context={"Mortes": mortes})

def delete_mortes(request, mortes_id):
   mortes = Mortes.objects.get(id=mortes_id)
   if request.method == "POST":
        if "confirm" in request.POST:
            mortes.delete()
            return redirect("home")

   return render(request, "delete_mortes.html", context={"Mortes": mortes})