from __future__ import absolute_import, division

from klein._plating import Plating
from klein._form import form
from klein._session import SessionProcurer
from klein.app import Klein, resource, route, run

from ._version import __version__ as _incremental_version


__all__ = (
    "Klein",
    "Plating",
    'form',
    'SessionProcurer',
    "__author__",
    "__copyright__",
    "__license__",
    "__version__",
    "resource",
    "route",
    "run",
)


# Make it a str, for backwards compatibility
__version__ = _incremental_version.base()

__author__ = "The Klein contributors (see AUTHORS)"
__license__ = "MIT"
__copyright__ = "Copyright 2016 {0}".format(__author__)
