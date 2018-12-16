from utils.rest_wrapper import RestWrapper
from .models import Poll


class PollView(RestWrapper):
    model = Poll
