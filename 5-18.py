def check_imported_class(filename, init_args, method_args, method_name, class_name):
    import_module = importlib.import_module(filename, package=None)
    TestClass = getattr(import_module, class_name)
    instance = test_class(*init_args)
    method = getattr(test_class, method_name)
    if method_args:
        result = method(instance,*method_args)
    else:
        result = method(instance)
    print(result)	
