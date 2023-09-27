def get_worker_actions(logs, id):
    result = []
    for log in logs:
        if 'actions' in log:
            for action in log['actions']:
                if 'part' in action and 'worker_id' in action and action['worker_id'] == id and action['part']:
                    worker_action = (action['worker_id'], action['part'])
                    if worker_action not in result:
                        result.append(worker_action)
    return result


if __name__ == "__main__":
    logs = [
        {
            'type': 'Brown Cowboy Boots',
            'actions': [
                {'worker_id': 1, 'part': 'heel'},
                {'worker_id': 2, 'part': 'toe box'},
            ]
        },
        {
            'type': 'Red Woman Boots',
            'actions': [
                {'worker_id': 2, 'part': 'tongue'},
                {'worker_id': 1, 'part': 'heel'}
            ]
        },
        {
            'type': 'Yellow Woman Boots',
            'actions': [
                {'worker_id': 2, 'part': ''},
                {'worker_id': 1}
            ]
        },
        {
            'type': 'Brown Woman Boots',
        }
    ]
    print(get_worker_actions(logs, 1))  # [(1, 'heel')]
    print(get_worker_actions(logs, 2))  # [(2, 'toe box'), (2, 'tongue')]
