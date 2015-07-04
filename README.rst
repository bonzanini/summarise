summarise - Python Text Summarisation module
============================================

This module is currently **experimental**. 

The API could change at any time. 


Installation
------------

Install with pip::

	pip install summarise

Install from github::

	git clone https://www.github.com/bonzanini/summarise
	cd summarise
	python setup.py install


Examples
--------

Code sample::

    from summarise import Summariser

    full_text = [['One', 'tokenized', 'sentence],
                 ['Another', 'sentence'],
                 ['The', 'quick', 'brown', 'fox', 'jumped']]
    summariser = Summariser(full_text)
    summary = summariser.summarise(size=2)


License
-------

MIT License, see LICENSE

