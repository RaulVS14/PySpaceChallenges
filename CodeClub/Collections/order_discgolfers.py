def order_discgolfers(round_scores):
    """
    Teeing order on all subsequent holes is determined by the scores on the previous hole,
    with the lowest score throwing first, and so on.
    If the previous hole was a tie,
    the scores are to be counted back until the order is resolved.
    """
    order = []
    if round_scores:
        previous_round = round_scores[-1]
        player_names = previous_round.keys()
        if len(player_names) == 1:
            return [player_names[0]]
        else:
            # TODO: figure out the logic
            return order_discgolfers()
    return order


if __name__ == '__main__':
    scores = [{
        'bob': 3,
        'patric': 2,
        'squidward': 4,
    }, {
        'bob': 3,
        'patric': 3,
        'squidward': 3,
    }, {
        'bob': 3,
        'patric': 3,
        'squidward': 2,
    }, {
        'bob': 3,
        'patric': 3,
        'squidward': 3,
    }]
    teeing_order = order_discgolfers(scores)
    for i, order in enumerate(teeing_order, start=2):
        print(f'Hole {i} Teeing Order:', ', '.join(order))
    assert order_discgolfers(scores) == ['squidward', 'patric', 'bob']
