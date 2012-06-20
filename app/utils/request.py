def saved(data):
    if data.get('save', '').strip():
        return True
    else:
        return False
