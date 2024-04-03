import getopt
import json
import sys
import settings
from help import print_help


def validate_args(args):
    if "-h" in args or "-H" in args or "--help" in args:
        return
    if "-v" in args or "-V" in args or "--version" in args:
        return
    if "-p" not in args and "-P" not in args and "--port" not in args:
        raise getopt.GetoptError("Http port is missing")
    if "-s" not in args and "-S" not in args and "--secret" not in args:
        raise getopt.GetoptError("Secret is missing")


def parse_arguments():
    try:
        args, _ = getopt.getopt(sys.argv[1:],
                                "hHvVp:P:s:S:",
                                [
                                    "help",
                                    "version",
                                    "port=",
                                    "secret="
                                ]
                                )
        used_args = [opt for opt, _ in args]
        validate_args(used_args)
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(2)
    return args


def patch_arguments(args):
    arg_dict = {}
    for opt, arg in args:
        if opt in ("-h", "-H", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-v", "-V", "--version"):
            print("Version: " + settings.VERSION)
            sys.exit()
        if opt in ("-p", "-P", "--port"):
            if not arg.isdigit():
                print("Invalid port number: " + arg)
                sys.exit(2)
            arg_dict["port"] = int(arg)
        if opt in ("-s", "-S", "--secret"):
            try:
                with open(arg, "r") as f:
                    json.load(f)
            except Exception as e:
                print(f"Error: {str(e)}")
                sys.exit(2)
            arg_dict["secret"] = arg
    return arg_dict
