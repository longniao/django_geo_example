ERROES = {
    '0': 'Success',
    '1': 'Failed',
    '2': 'Some fields are empty',
}

def result(code):
    '''
    response result
    '''
    code = str(code)
    return dict(
        code=int(code),
        msg=ERROES.get(code,ERROES['0']),
    )