from src.models.model import Quote, User, Channel
from peewee import fn


def quote(**kwargs):
    channel = kwargs.get("channel", "testchannel")
    quote_data = Quote.select().where(Quote.channel == Channel.get(channel=channel).id).order_by(fn.Random()).limit(1)
    if len(quote_data) == 0:
        return "No quotes found. Why not add one with '!addquote [quote]'?"
    else:
        quote_data = quote_data[0]
        quote = quote_data.message
        quote_number = quote_data.id
        game = quote_data.game
        resp = "Quote #{0}: \"{1}\" [{2}]".format(quote_number, quote, game)
        return resp
