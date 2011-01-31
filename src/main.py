#!/usr/bin/python2
#
# Copyright (C) 2010-2011 Ben Breslauer
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys, string, signal, os
from optparse import OptionParser

from PyQt4.QtCore import QT_VERSION_STR
from PyQt4.QtGui import QApplication

import config
from Pysciplot import Pysciplot




def setupOptions():
    usage = "usage: %prog [options] project-file.psp"

    parser = OptionParser(usage)

    parser.add_option("-d", type="int", dest="debug", metavar="[level]", help="Debug level (between 0 and 3)")

    return parser.parse_args()



if __name__ == "__main__":
    # check to make sure we are using at least Qt 4.6.1, as there is a bugfix in that version that causes
    # qheaderview logicalindices to refactor when removing a column
    qtVersion = string.split(QT_VERSION_STR, ".")
    if qtVersion < ['4',  '6',  '1']:
        print "This application requires at least Qt version 4.6.1.  You are running " + QT_VERSION_STR + "."
        sys.exit()
    
    (options, args) = setupOptions()
    
    config.debugLevel = options.debug
    
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QApplication(sys.argv)
    app.window = Pysciplot()
    app.window.setup()
    app.window.show()
    
    if len(args) > 0:
        # load the first arg (which should be a file) as a project
        if args[0].split('.')[-1] == "psp":
            app.window.loadProject(os.path.abspath(args[0]), False)

    sys.exit(app.exec_())

