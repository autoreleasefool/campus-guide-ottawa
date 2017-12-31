"""Path utilities."""


import os


def get_root_dir():
    """Get the module root directory."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..')


def get_asset_dir(component):
    """Get the asset directory path.

    :param component:
        either 'app' or 'server'
    :type component:
        `str`
    """
    return os.path.join(get_root_dir(), 'assets_{}'.format(component))


def get_output_dir():
    """Get the output directory path."""
    return os.path.join(get_root_dir(), 'output')
