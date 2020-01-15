def emoji_converter (message):

    message_break = message.split(" ")

    emoji = {
        ':)':'😀',
        ':(':'☹️',
        ':/':'😕',
        ';)':'😉',
        ':o':'😮',
        ':O':'😧',
        ':0':'😲',
        ':p':'😛',
        ':P':'😝',
        ';(':'😒',
        ';p':'😜',
        ';P':'🤪',
        ':N':'🤐',
        ':|':'😐',
        '-_-':'😑',
        ':':'😶',
        'FIRE':'🔥',
        'ICE':'🧊',
        'CAT':'😺',
        'POOP':'💩',
        'GHOST':'👻',
        'SKULL':'💀',
        'ALIEN':'👽',
        'SEE':'👀',
        'EYE':'👁',
        'EYES':'👀',
        'BRAIN':'🧠',
        'RAT':'🐭',
        'BUTTERFLY':'🦋',
        'APPLE':'🍎',
        'PEAR':'🍐',
        'LEMON':'🍋',
        'BANANA':'🍌',
        'WATERMELON':'🍉',
        'SOCCER':'⚽',
        'BASKETBALL':'🏀',
        'BALL':'🏀',
        'BASEBALL':'⚾️',
        'VOLLEYBALL':'🏐',
        'FOOTBALL':'🏉',
        'TENNIS':'🎾',
        'CAT':'😸',
        'DOG':'🐶',
        'BUNNY':'🐰',
        'FOX':'🦊',
        'BEAR':'🐻',
        'PANDA':'🐼',
        'KOALA':'🐨',
        'TIGER':'🐯',
        'LION':'🦁',
        'MONKEY':'🐵',
        'PENGUIN':'🐧',
        'GOOSE':'🦆',
        'DOLPHIN':'🐬',
        'EARTH':'🌎',
        'TORNADO':'🌪',
        'STAR':'⭐️',
         'LIGHTNING':'⚡️',
        'BANG':'💥',
        'WET':'💦',
        'RAIN':'💧',
        'SMOKE':'💨',
        'WAVE':'🌊',
        'MOON':'🌙',
        'SUN':'🌞'

    }
    out_msg=''
    for item in message_break:
        out_msg += emoji.get(item.upper(),item) + " "

    return out_msg;

message = input("Enter your message: ")
while 'quit'.upper() != message.upper():
  print(emoji_converter(message))
  message = input("Enter your message: ")

print('Bye 👋🏼👋🏼')


