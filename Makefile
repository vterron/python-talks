# Inspired by Stephan Bourduas's LaTeX Makefile:
# http://www.iml.ece.mcgill.ca/~stephan/node/13

SHELL := /bin/bash

# Run all Python scripts, save output
OUTPUTS_SCRIPT=./generate-outputs.py
CODE_ROOT=./code/
CODE_OUTPUT=output

PDFLATEX=pdflatex
PDFLATEX_OPTS=-interaction=nonstopmode -halt-on-error -shell-escape

TEX_FILE=python-clases.tex

.PHONY: all pdf clean

all : pdf

pdf: $(TEX_FILE)
	$(OUTPUTS_SCRIPT) $(CODE_ROOT) $(CODE_OUTPUT)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)
	$(PDFLATEX) $(PDFLATEX_OPTS) $(TEX_FILE)

clean:
	rm -fv *.{aux,log,nav,out,snm,toc,vrb}
	rm -rf $(CODE_ROOT)/*/$(CODE_OUTPUT)
