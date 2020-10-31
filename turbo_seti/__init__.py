from .find_doppler import seti_event, FindDoppler, helper_functions
from .find_event import find_event, plot_event, plot_event_pipeline, plot_event_pipeline, read_dat
from .log import logger_group

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('turbo_seti').version
except DistributionNotFound:
    __version__ = '0.0.0 - please install via pip/setup.py'
