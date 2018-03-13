schema = {
    'guilds': {
        'id': 1,
        'members': ['memberId1', 'memberId2'],
        'store': 'storeId',
        'waifus': 'waifusId',
        'menu': 'menuId',
    },
    'members': {
        'id': 101,
        'guilds': ['barglebotGuildId1, bargleBotGuildId2?']
    },
    'waifus': {
        'guildId': {
            'memberId': 'member2Id',
            'member2Id': 'memberId'
        }
    },
    'stores': {
        'guildId': {
            'store': {

            }
        }
    },
    'inventory': {
        'guildId': {
            'memberId': {
                'item1': 'meme'
            }
        }
    },
    'items': [
        {
            'guildId': 101,

        }
    ]
}