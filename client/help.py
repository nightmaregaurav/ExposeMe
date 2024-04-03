def print_help():
    print('''Usage: expose-my [options]\n
Options:\n
\t-h, -H, --help          Display help\n
\t-v, -V, --version       Display version\n
Arguments:\n
\t-u, -U, --userid        User ID (required)\n
\t-a, -A, --apikey        API key (required)\n
\t-p, -P, --port          Port number (required)\n
\t-s, -S, --subdomains    Comma separated list of subdomains one of which will be used given that it is available.
                          Priority is from left to right (required if -n/-N/--no-random is used)\n
\t-n, -N, --no-random     Do not use random subdomains if provided subdomains are not available.
                          (Cannot be used without -s/-S/--subdomains)''')
