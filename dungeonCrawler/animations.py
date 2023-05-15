from time import sleep
import os


def clear(): return os.system('cls')


def play(animation, speed=0.075):
    for step in animation:
        clear()
        print(step)
        sleep(speed)
    clear()


morningAni = [
    ' 😔',
    ' 😪',
    ' 😔',
    ' 😪',
    ' 😔',
    ' 😑',
    ' 😑',
    ' 😒',
    ' 😒'
]

fightAni = [
    '😠      👹',
    '😠      👹',
    '😠      👹',
    ' 😠    👹 ',
    '  😠  👹  ',
    '   😠🤜👹  ',
    '  😠   👹  ',
    ' 😡🤛👹   ',
    '  😠  👹  ',
    '   😠🤜💀  ',
    '  😠   💀  ',
    '  😠   💀  '
]

fireballAni = [
    '😠      👹',
    '😠      👹',
    '😠🔥    👹',
    '😠🔥    👹',
    '😠 🔥   👹',
    '😠  🔥  👹',
    '😠   🔥 👹',
    '😠    🔥👹',
    '😠      💥',
    '😠      💥',
    '😠      💀',
    '😠      💀'
]
