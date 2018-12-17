from django.urls import reverse, resolve


class TestUrls:
    def test_polls_url(self):
        path = reverse('polls')
        assert resolve(path).view_name == 'polls'

    def test_polls_pk_url(self):
        path = reverse('polls', kwargs={'pk': 1})
        assert resolve(path).view_name == 'polls'

