import json

from django.core import serializers
from django.http import HttpResponse
from django.views.generic import View


class RestWrapper(View):
    model = None

    def post(self, request, *args, **kwargs):
        try:
            obj = self.model(**json.loads(request.body))
            obj.save()
            res = serializers.serialize('json', [obj])
            created = json.loads(res)[0]
            return HttpResponse(json.dumps(created), status=201)
        except Exception:
            return HttpResponse('Can\'t create', status=400)

    def get(self, request, *args, **kwargs):
        obj = self.model.objects
        limit = None
        for attr, val in dict(request.GET).items():
            if attr == 'limit':
                limit = int(val[0])
            elif attr == 'order_by':
                obj = obj.order_by(val[0])
            else:
                obj = obj.filter(**{attr: val[0]})
        if limit is not None:
            obj = obj[:limit]
        response = json.loads(serializers.serialize('json', obj))
        response = [res['fields'] for res in response]
        return HttpResponse(response, status=200)

    def put(self, request, *args, **kwargs):
        try:
            obj = self.model.objects.get(pk=kwargs['id'])
            data = json.loads(request.body)
            for attr, val in data.items():
                setattr(obj, attr, val)
            obj.save()
            return HttpResponse('Success', status=200)
        except Exception:
            return HttpResponse('Error updating', status=400)

    def delete(self, request, *args, **kwargs):
        try:
            obj = self.model.objects.get(pk=kwargs['id'])
            obj.delete()
            return HttpResponse('', status=204)
        except Exception:
            return HttpResponse('Error DELETE', status=400)
