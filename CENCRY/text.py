import time

vowels = ['a', 'e', 'i', 'o', 'u']
consonants = [
    'b', 'c', 'd',
    'f', 'g', 'h',
    'j', 'k', 'l',
    'm', 'n', 'p',
    'q', 'r', 's',
    't', 'v', 'w',
    'x', 'y', 'z'
]


def encrypt(word):
    t0 = time.process_time()
    utils = {
        'vowels': {
            'start': 0,
            'stop': len(vowels)
        },
        'consonants': {
            'start': 0,
            'stop': len(consonants)
        },
        'final': []
    }
    k = len(word)
    value = list(word)
    v_list = vowels[:] * 1000
    c_list = consonants[:] * 1000

    for i in range(k):
        if vowels.__contains__(value[i]):
            x = v_list.index(value[i], utils['vowels']['start'], utils['vowels']['stop'])
            utils['vowels']['start'] = utils['vowels']['stop']
            utils['vowels']['stop'] *= 2
            utils['final'].append(c_list[x])

        else:
            y = c_list.index(value[i], utils['consonants']['start'], utils['consonants']['stop'])
            utils['consonants']['start'] = utils['consonants']['stop']
            utils['consonants']['stop'] *= 2
            utils['final'].append(v_list[y])

    return {
        'result': "".join(utils['final']),
        'time': f"{time.process_time() - t0} (s)"
    }


print(encrypt("baax"))
print(encrypt('aaa'))
print(encrypt('bnh'))
