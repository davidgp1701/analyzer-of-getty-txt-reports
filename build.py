# This is the builder script for the Report Analyzer of TXT files
#
# This code is licensed under an Apache 2.0 license. Please, refer to the LICENSE.TXT file for more information
#

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

default_task = ["clean", "publish"]

@init
def initialize(project):
    project.build_depends_on('mockito')
