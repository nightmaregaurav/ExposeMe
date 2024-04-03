import getopt
import sys
import settings
from help import print_help


def validate_args(args):
    if "-h" in args or "-H" in args or "--help" in args:
        return
    if "-v" in args or "-V" in args or "--version" in args:
        return
    if "-u" not in args and "-U" not in args and "--userid" not in args:
        raise getopt.GetoptError("User ID is missing")
    if "-a" not in args and "-A" not in args and "--apikey" not in args:
        raise getopt.GetoptError("API key is missing")
    if "-p" not in args and "-P" not in args and "--port" not in args:
        raise getopt.GetoptError("Port is missing")
    if (("-s" not in args and "-S" not in args and "--subdomains" not in args)
            and ("-n" in args or "-N" in args or "--no-random" in args)):
        raise getopt.GetoptError("No subdomains provided for no-random mode")


def parse_arguments():
    try:
        args, _ = getopt.getopt(sys.argv[1:],
                                "hvHVu:U:a:A:p:P:s:S:nN",
                                [
                                    "help",
                                    "version",
                                    "userid=",
                                    "apikey=",
                                    "port=",
                                    "subdomains=",
                                    "no-random"
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

        if opt in ("-u", "-U", "--userid"):
            arg_dict["userid"] = arg
        if opt in ("-a", "-A", "--apikey"):
            arg_dict["apikey"] = arg
        if opt in ("-p", "-P", "--port"):
            if not arg.isdigit():
                print("Invalid port number: " + arg)
                sys.exit(2)
            arg_dict["port"] = int(arg)
        if opt in ("-s", "-S", "--subdomains"):
            subdomains = arg.split(",")
            subdomains = [subdomain.strip() for subdomain in subdomains]
            for subdomain in subdomains:
                if not subdomain.isalnum():
                    print("Invalid subdomain found: " + subdomain)
                    sys.exit(2)
            arg_dict["subdomains"] = subdomains
        else:
            arg_dict["subdomains"] = []
        if opt in ("-n", "-N", "--no-random"):
            arg_dict["no-random"] = True
        else:
            arg_dict["no-random"] = False
