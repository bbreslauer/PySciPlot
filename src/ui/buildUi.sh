#!/bin/bash
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


# Get list of files to convert
if [ $# -gt 0 ]
then
    files=$@
else
    files=`ls *.ui`
fi

# convert ui files to py source code
#for file in `ls *.ui`
for file in $files
do
    echo ${file}
    pyuic4 -o ${file}.py ${file}
    
    # remove all connectSlotsByName entries in py files
    sed '/connectSlotsByName/d' ${file}.py > ${file}.py.new
    rm ${file}.py
done

# rename files
#rename -f s/ui.py.new/py/g *.ui.py.new
rename ui.py.new py *.ui.py.new

