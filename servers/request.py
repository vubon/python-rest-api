from settings.settings import ALLOWED_HOSTS


def split_domain(allowed_hosts):
    """
    By this function will split host from a list
    :param allowed_hosts:
    :return:
    """
    for host in allowed_hosts:
        if host == "*":
            return "0.0.0.0"
        return host


def get_host():
    # Allow variants of localhost if ALLOWED_HOSTS is empty then send default host and port
    allowed_hosts = ALLOWED_HOSTS
    if not allowed_hosts:
        allowed_hosts = ['localhost', '127.0.0.1', '[::1]']

    domain = split_domain(allowed_hosts)

    return domain

