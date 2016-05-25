from src.models.model import Quote, User, Channel
from src.lib.twitch import Twitch


def addquote(args, **kwargs):
    username = kwargs.get("username", "testuser")
    channel = kwargs.get("channel", "testchannel")
    quote = unicode(args[0].strip().strip("\"").strip("\'"), 'utf-8')
    if len(quote) > 200:
        return "Let's keep it below 200 characters?"
    game = "offline"
    stream = Twitch(channel, username).stream()["stream"]
    print stream
    if stream is not None:
        game = stream["game"]
    print dict(User.get_or_create(username=username.lower())[0])
    username_id = User.get_or_create(username=username.lower()).id
    channel_id = Channel.get_or_create(channel=channel).id
    Quote.create(username=username_id, channel=channel_id, message=quote, game=game)
    return "{0} added!".format(quote)
