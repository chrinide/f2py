from __future__ import absolute_import

def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('fparser',parent_package,top_path)
    config.add_data_files('log.config')
    return config
