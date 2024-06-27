from django.conf import settings
from django.shortcuts import render

from log_app.forms import SearchForm
from log_app.models import Log, Message


def index(request):
    template = 'log_app/index.html'
    title = 'Просмотр логов'
    form = SearchForm() 
    query, response, response_lst = None, None, []
    if 'query' in request.GET: 
        form = SearchForm(request.GET) 
        if form.is_valid(): 
            query = form.cleaned_data['query']
    if query:
        response_lst.extend(
            list(
                row.as_dict() for row in Log.objects.filter(
                    address=query.upper()).order_by('int_id', 'created')
                )
            )
        messages = Message.objects.filter(
            int_id__in=set(list([x['int_id'] for x in response_lst]))
        ).order_by('int_id', 'created')
        response_lst.extend(list(row.as_dict() for row in messages))
        response = sorted(response_lst, key=lambda x: x['created'])
    context = {
        'title': title,
        'text': 'Просмотр логов',
        'logs': response[:settings.RESPONSE_LIMIT],
        'len_response': len(response) > settings.RESPONSE_LIMIT
    }
    return render(request, template, context)
