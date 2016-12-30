PYTHON=python

package:
	python setup.py sdist bdist_wheel

release:
	@if git tag | grep -q `$(PYTHON) setup.py -V` ; then\
		echo "Already released this version.";\
		echo "Update the version number and try again.";\
		exit 1;\
	fi
	@if [ `git status --short | wc -l` != 0 ]; then\
		echo "Uncommited code. Aborting." ;\
		exit 1;\
	fi
	$(PYTHON) setup.py bdist_wheel upload
	$(PYTHON) setup.py sdist --formats=zip,gztar,bztar upload
	git tag `$(PYTHON) setup.py -V`
	git push
	git push --tags
