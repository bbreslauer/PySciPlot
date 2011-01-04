#!/bin/bash

# convert all ui files to py source code
for file in `ls *.ui`
do
    pyuic4 -o ${file}.py ${file}
    
    # remove all connectSlotsByName entries in py files
    sed '/connectSlotsByName/d' ${file}.py > ${file}.py.new
    rm ${file}.py
done

# rename files
#rename -f s/ui.py.new/py/g *.ui.py.new
rename ui.py.new py *.ui.py.new

