from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
from survey.models import *
from random import randint
from django.db.utils import IntegrityError
from django.db.models import Count

# Create your views here.
class ResponseForm(forms.Form):
    good = forms.BooleanField(label='Is this definition good', required=False)
    comment = forms.CharField(widget=forms.Textarea, label='Comments', required=False)
    term_id = forms.IntegerField(widget=forms.HiddenInput)

def landing_page(request):
    r = request.session.get('id', False)
    if r == False:
        resp = Respondant.objects.create()
        request.session['id'] = resp.id
    return render(request, 'landing.html', {'token': r})

def clear_session(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return redirect(landing_page)

def term_review(request):
    error = ''
    # Get our respondant out of cookie
    r = request.session.get('id', False)
    if r == False:
        return render(request, 'cookie_error.html')
    resp = Respondant.objects.get(pk=r)

    # parse the last review
    if request.method == 'POST':
        form = ResponseForm(request.POST)
        if form.is_valid():
            term = Term.objects.get(pk=form.cleaned_data['term_id'])
            try:
                Response.objects.create(respondant=resp,
                                        term=term,
                                        is_good=form.cleaned_data['good'],
                                        comment=form.cleaned_data['comment'])
            except IntegrityError:
                error = "You already submitted a review for that term"

    # check to see if user has submitted enough reviews
    max_reviews = Setting.objects.all().first().terms_per_user
    num_reviews = Response.objects.filter(respondant=resp).count()
    if num_reviews >= max_reviews:
        return render(request, 'thank_you.html')

    # get a random term to review from the terms with least responses
    query = Term.objects.exclude(response__respondant=resp)
    query = query.annotate(num_reviews=Count('response'))
    lowest_reviews = query.order_by('num_reviews').first().num_reviews
    query = query.filter(num_reviews=lowest_reviews)
    count = query.count()
    random_index = randint(0, count - 1)
    term = query[random_index]
    form = ResponseForm({'term_id': term.id})
    return render(request, 'review.html', {'error': error, 'term': term, 'form': form})
