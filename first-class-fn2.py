def head(title):
    def description(desr):
        print('{}:{}'.format(title, desr))
    return description
result1 = head('Kenyan independance')
result1('gained in 1963')