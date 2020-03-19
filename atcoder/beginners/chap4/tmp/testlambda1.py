# CF https://qiita.com/macinjoke/items/1be6cf0f1f238b5ba01b


def args_logger(f):
    def wrapper(*args, **kwargs):
        f(*args, **kwargs)
        print("args: {} kwargs: {}".format(args, kwargs))
    return wrapper


@args_logger
def print_message(msg):
    print(msg)


if __name__ == "__main__":
    print_message('Hello')
