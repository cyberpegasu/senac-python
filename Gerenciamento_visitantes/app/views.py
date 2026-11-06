from datetime import date
from uuid import uuid4
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms.createvisitorform import CreateVisitorForm
from .forms.update_visitor_form import UpdateVisitorForm
from .models import Visitor, TicketType


def home(request):
    return render(request, 'home.html')


def visitors(request):
    search = request.GET.get('name_or_cpf', '').strip()
    ticket_type = request.GET.get('ticket_type', '0')

    visitantes = Visitor.objects.all()

    if search:
        visitantes = visitantes.filter(
            Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
            | Q(cpf__contains=search)
        )

    tipos_validos = {str(valor) for valor in TicketType.values}

    if ticket_type in tipos_validos:
        visitantes = visitantes.filter(
            ticket_type=int(ticket_type)
        )
    else:
        ticket_type = '0'

    contexto = {
        'visitors': visitantes,
        'search': search,
        'ticket_type': ticket_type,
    }

    return render(request, 'visitors.html', contexto)


def create_visitor(request):
    if request.method == 'POST':
        visitor_form = CreateVisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor = visitor_form.save(commit=False)
            visitor.ticket_number = str(uuid4())
            visitor.save()

            return redirect('visitors')
    else:
        visitor_form = CreateVisitorForm()

    response = {
        'form': visitor_form,
    }

    return render(request, 'create-visitor.html', response)


def update_visitor(request, id):
    visitor = get_object_or_404(Visitor, pk=id)

    if request.method == 'POST':
        visitor_form = UpdateVisitorForm(request.POST, istance=visitor)

        if visitor_form.is_valid():
            visitor_form.save()
            return redirect('visitors')

    else:
        visitor_form = UpdateVisitorForm(instance=visitor)

    response = {
        'form': visitor_form,
        'ticket_number': visitor.ticket_number
    }

    return render(request, 'update-visitor.html', response)


def delete_visitor(request, id):
    visitor = get_object_or_404(Visitor, pk=id)
    visitor.delete()

    return redirect('visitors')


def estatisticas(request):
    visitantes = Visitor.objects.all()

    # Total de visitantes cadastrados
    total_visitantes = visitantes.count()

    # Quantidade de ingressos por categoria
    ingressos_normal = visitantes.filter(
        ticket_type=TicketType.NORMAL
    ).count()

    ingressos_vip = visitantes.filter(
        ticket_type=TicketType.VIP
    ).count()

    ingressos_premium = visitantes.filter(
        ticket_type=TicketType.PREMIUM
    ).count()

    # Cálculo da média de idade
    hoje = date.today()
    soma_idades = 0
    quantidade_com_nascimento = 0

    for visitante in visitantes:
        nascimento = visitante.birth_date

        if nascimento:
            idade = (
                hoje.year
                - nascimento.year
                - (
                    (hoje.month, hoje.day)
                    < (nascimento.month, nascimento.day)
                )
            )

            soma_idades += idade
            quantidade_com_nascimento += 1

    if quantidade_com_nascimento > 0:
        media_idade = round(
            soma_idades / quantidade_com_nascimento,
            1
        )
    else:
        media_idade = 0

    # Dados enviados para o template HTML
    contexto = {
        'total_visitantes': total_visitantes,
        'ingressos_normal': ingressos_normal,
        'ingressos_vip': ingressos_vip,
        'ingressos_premium': ingressos_premium,
        'media_idade': media_idade,
    }

    return render(
        request,
        'estatisticas.html',
        contexto
    )

