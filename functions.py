def var_args(name, *args):
    print(name)
    print(args)

def var_args2(name, **kwargs):
    print(name)
    print(kwargs['description'], kwargs['feedback'])


var_args('Mark', 'loves python', None, True)

var_args2('Mark', description="loves python", feedback=None)