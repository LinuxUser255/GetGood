#!/usr/bin/env bash

# for loop in bash scripting for i in range 1 - 5
for (( i=1; i<=5; i++ )); do
    # create a new file with touch, the file names are
    # powell_metaclass.py
    # powell_decorator.py
    # powell_generator.py
    # powell_context_manager.py
    touch powell_metaclass.py powell_decorator.py powell_generator.py powell_context_manager.py

done