from django.test import RequestFactory
from django.urls import reverse
import pytest

from polls.views import PollView


@pytest.mark.django_db
class TestView:
    def test_create_fail_poll(self):
        path = reverse('polls')
        request = RequestFactory().post(path, {'wrong': 'abc'}, content_type='application/json')
        response = PollView.as_view()(request)
        assert response.status_code == 400

    def test_create_success_poll(self):
        path = reverse('polls')
        request = RequestFactory().post(path, {'name': 'abc', 'stars': 5, 'views': 3}, content_type='application/json')
        response = PollView.as_view()(request)
        assert response.status_code == 201

    def test_get_success_poll(self):
        path = reverse('polls', kwargs={'pk': 1})
        request = RequestFactory().post(path, {'name': 'abc', 'stars': 5, 'views': 3}, content_type='application/json')
        PollView.as_view()(request)
        request = RequestFactory().get(path)
        response = PollView.as_view()(request, pk=1)
        assert response.status_code == 200

    def test_put_success_poll(self):
        path = reverse('polls')
        request = RequestFactory().post(path, {'name': 'abc', 'stars': 5, 'views': 3}, content_type='application/json')
        PollView.as_view()(request)
        path = reverse('polls', kwargs={'pk': 1})
        request = RequestFactory().put(path, {'name': 'xvz', 'stars': 5, 'views': 3}, content_type='application/json')
        response = PollView.as_view()(request, pk=1)
        assert response.status_code == 200

    def test_delete_success_poll(self):
        path = reverse('polls')
        request = RequestFactory().post(path, {'name': 'abc', 'stars': 5, 'views': 3}, content_type='application/json')
        PollView.as_view()(request)
        path = reverse('polls', kwargs={'pk': 1})
        request = RequestFactory().delete(path)
        response = PollView.as_view()(request, pk=1)
        assert response.status_code == 204

    def test_delete_error_poll(self):
        path = reverse('polls')
        request = RequestFactory().post(path, {'name': 'abc', 'stars': 5, 'views': 3}, content_type='application/json')
        PollView.as_view()(request)
        path = reverse('polls', kwargs={'pk': 2})
        request = RequestFactory().delete(path)
        response = PollView.as_view()(request, pk=2)
        assert response.status_code == 400
