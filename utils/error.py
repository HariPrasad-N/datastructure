def error_message(error,message):
    """
        Colours the error and displays the error message
    """
    print("\033[91m {}\033[00m".format(error)+" : "+message)
    return