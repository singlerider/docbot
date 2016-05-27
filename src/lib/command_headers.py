import globals

commands = {
    '!followers': {
        'limit': 30,
        'user_level': 'mod',
        'return': 'command',
        'argc': 0,
        'usage': '!followers',
        'user_limit': 30,
    },
    '!follower': {
        'limit': 0,
        'return': 'command',
        'argc': 1,
        'usage': '!follower [username]',
        'user_level': 'mod'
    },
    '!uptime': {
        'limit': 15,
        'return': 'command',
        'argc': 0,
        'usage': '!uptime',
        'user_limit': 30,
    },
    '!stream': {
        'limit': 0,
        'return': 'command',
        'argc': 0,
        'usage': '!stream'
    },
    '!caster': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!caster [streamer_username]',
        'user_level': 'mod'
    },
    '!addquote': {
        'limit': 0,
        'argc': 1,
        'return': 'command',
        'usage': '!addquote [quote]',
        'user_level': 'mod'
    },
    '!quote': {
        'limit': 0,
        'argc': 0,
        'return': 'command',
        'usage': '!quote'
    }
}

user_cooldowns = {"channels": {}}


def initalizeCommands(config):
    for channel in config['channels']:
        globals.CHANNEL_INFO[channel.lstrip("#")] = {"drop": {}}
        user_cooldowns["channels"][channel] = {"commands": {}}
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
            if "user_limit" in commands[command]:
                user_cooldowns["channels"][channel]["commands"][command] = {
                    "users": {}}

if __name__ == "__main__":  # pragma: no cover
    print "{\n" + ",\n".join(["    \"" + key + "\": \"" + commands[key][
        "usage"] for key in commands]) + "\"\n}"
