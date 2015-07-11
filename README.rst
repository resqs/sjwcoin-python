sjwcoin-python is a fork of bitcoin-python ( and sjwcoin-python) : https://github.com/laanwj/bitcoin-python

It is a set of Python libraries that allows easy access to the
sjwcoin peer-to-peer cryptocurrency client API.


Documentation
===========================

The documentation for bitcoin-python can be found here (or built from sources) :

http://jcsaaddupuy.github.io/sjwcoin-python/doc/index.html


Installation instructions
===========================

sjwcoin-python uses setuptools for the install script. There are no dependencies apart from Python itself.

::

  $ python setup.py build
  $ python setup.py install
  

Pypi / Cheeseshop
==================

It is possible to install the package through Pypi (cheeseshop), see http://pypi.python.org/pypi?:action=display&name=sjwcoin-python
::
 $ pip install sjwcoin-python
 # if not working, try
 $ pip install --pre sjwcoin-python

Connection to sjwcoin-qt
=========================

If you want to connect to sjwcoin-qt, add server=1 in your sjwcoin.conf
::

 rpcuser=sjwcoinrpc
 rpcpassword=A RANDOM GENERATED PASSWORD
 server=1

TODO
======
These things still have to be added:

- SSL support (including certificate verification) for managing remote sjwcoin daemons.

