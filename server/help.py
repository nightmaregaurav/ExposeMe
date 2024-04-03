def print_help():
    print('''Usage: expose-from [options]\n
Options:\n
\t-h, -H, --help          Display help\n
\t-v, -V, --version       Display version\n
Arguments:\n
\t-p, -P, --port          Http port number (required)\n
\t-s, -S, --secret        Path to secret file that contains allowed userId and apiKey (required)''')
