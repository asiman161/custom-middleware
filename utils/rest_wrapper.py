import json

from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View


class RestWrapper(View):
    model = None

    def post(self, request, *args, **kwargs):
        try:
            queryset = self.model(**json.loads(request.body))
            queryset.save()
            res = serializers.serialize('json', [queryset])
            created = json.loads(res)[0]
            return HttpResponse(json.dumps(created), status=201)
        except:
            return HttpResponse('Can\'t create', status=400)

    def get(self, request, pk=None, *args, **kwargs):
        queryset = self.model.objects
        if pk is not None:
            queryset = queryset.filter(pk=pk)[:1]
        else:
            limit = None
            if len(dict(request.GET).items()) == 0:
                queryset = queryset.all()
            for attr, val in dict(request.GET).items():
                if attr == 'limit':
                    limit = int(val[0])
                elif attr == 'order_by':
                    queryset = queryset.order_by(val[0])
                else:
                    queryset = queryset.filter(**{attr: val[0]})
            if limit is not None:
                queryset = queryset[:limit]
        response = json.loads(serializers.serialize('json', queryset))
        response = [res['fields'] for res in response]
        if len(response) > 0:
            return HttpResponse(response, status=200)
        else:
            return HttpResponse('Not Found', status=404)

    def put(self, request, pk, *args, **kwargs):
        try:
            queryset = self.model.objects.get(pk=pk)
            data = json.loads(request.body)
            for attr, val in data.items():
                setattr(queryset, attr, val)
            queryset.save()
            response = json.loads(serializers.serialize('json', [queryset]))[0]
            return HttpResponse(json.dumps(response['fields']), status=200)
        except:
            return HttpResponse('Error updating', status=400)

    def delete(self, request, *args, **kwargs):
        try:
            queryset = self.model.objects.get(pk=kwargs['pk'])
            queryset.delete()
            return HttpResponse('', status=204)
        except:
            return HttpResponse('Error DELETE', status=400)
