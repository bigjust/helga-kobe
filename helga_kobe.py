import random

from helga.plugins import command


@command('kobe', help='I\'m thinkin\' of tryin\' out for a scholarship. ')
def kobe(client, channel, nick, message, cmd, args):
    """
    swooosh.
    """
    return 'o/ {ballin} `-'.format(ballin=' ' * random.randint(1, 25))
