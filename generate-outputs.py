#! /usr/bin/env python

# Author: Victor Terron (c) 2014
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" Walk the ROOT directory bottom-up and execute all Python scripts (*.py)
we come across. The output of each script (both standard output and error)
is written to a text file of the same name but without extension, stored in
the OUTPUT directory (relative to the directory where the script is located).
Lines are wrapped so that every line is at most 70 characters long.

"""

import os.path
import subprocess
import sys
import textwrap

ROOT = sys.argv[1]
OUTPUT = sys.argv[2]

for root, dirs, files in os.walk(ROOT, topdown=False):
    for file_ in sorted(files):
        basename, ext = os.path.splitext(file_)
        if ext == '.py':

            # Create output directory, if needed
            output_dir = os.path.join(root, OUTPUT)
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)

            path = os.path.join(root, file_)
            print "Script:", path

            args = ['python', path]
            output = os.path.join(output_dir, basename)
            kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            process = subprocess.Popen(args, **kwargs)
            out = process.communicate()[0]

            with open(output, 'wt') as fd:
                for line in out.splitlines():
                    for wrapped_line in textwrap.wrap(line):
                        fd.write(wrapped_line + '\n')
