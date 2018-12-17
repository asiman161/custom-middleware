import pytest

from polls.models import Poll


@pytest.mark.django_db
class TestModels:
    def test_create(self):
        poll = Poll(
            views=10,
            stars=10,
            name='some',
        )
        poll.save()
        assert Poll.objects.get(pk=poll.pk)
