from django.contrib.auth import get_user_model
from django.db import connections
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Max

from bugs.models import Bug
from features.models import Feature

# Create your views here.
User = get_user_model()

def graph(request):
    return render(request, 'graphs.html')


def number_of_graph(request):
    user_count = User.objects.all().count()
    bug_count = Bug.objects.all().count()
    feature_count = Feature.objects.all().count()
    bug_max = Bug.objects.all().aggregate(Max('upvotes'))
    feature_max = Feature.objects.all().aggregate(Max('upvotes'))
    
    bugs_and_features_todo = (Bug.objects.filter(status="todo").count()) + (Feature.objects.filter(status="todo").count())
    bugs_and_features_doing = (Bug.objects.filter(status="doing").count()) + (Feature.objects.filter(status="doing").count())
    bugs_and_features_done = (Bug.objects.filter(status="done").count()) + (Feature.objects.filter(status="done").count())
    
    
     
    features_max_upvote = feature_max
    labels1 = ["Users", "Bugs", "Features"]
    labels2 = ["Bugs", "Features"]
    labels3 = ["To do", "Doing", "Done"]
    default = [user_count, bug_count, feature_count]
    max_values = [bug_max["upvotes__max"], feature_max["upvotes__max"]]
    bugs_and_feature_status = [bugs_and_features_todo, bugs_and_features_doing, bugs_and_features_done]
    
    
    data={
        "labels1": labels1,
        "labels2": labels2,
        "labels3": labels3,
        "default": default,
        "max_values": max_values,
        "bugs_and_feature_status": bugs_and_feature_status
    }
    return JsonResponse(data, safe=False)