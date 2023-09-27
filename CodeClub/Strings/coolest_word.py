def coolness_factor(word):
    return len(set(word))


def coolest_word(words):
    if words:
        return max(words, key=coolness_factor)
    return


if __name__ == '__main__':
    assert coolest_word(['expectation', 'discomfort', 'half', 'decomposition']) == "decomposition"
    assert not coolest_word([])
