.PHONY: verify paper

PYTHON_EXECUTABLE ?= python3
TEX_COMPILER ?= pdflatex

verify:
	$(PYTHON_EXECUTABLE) checks/verify_127.py

paper:
	mkdir -p build
	$(TEX_COMPILER) -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
	$(TEX_COMPILER) -no-shell-escape -interaction=nonstopmode -halt-on-error -output-directory=build paper/main.tex
