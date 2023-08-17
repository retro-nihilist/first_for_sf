#Не Удалять то что ниже
family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
 ]
#Не удалять то что выше

def filter_family (x):
    y=list()
    """
    for i in x:
        if i in family_list:
            y.append(i)
        else: pass
        """
    lambda_filter = lambda x: x in family_list
    y = list(filter(lambda_filter, x))
    
    return y


print(filter_family(['newborn registration', 'parking permit', 'maternity capital', 'tax benefit', 'medical policy']))
## ['parking permit', 'maternity capital', 'tax benefit']


#print(filter_family(['reimbursement of expenses', 'parking permit', 'maternity capital', 'medical policy']))
## ['reimbursement of expenses', 'parking permit', 'maternity capital']