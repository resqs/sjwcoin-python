****************************
  Examples
****************************

A basic program that uses ``python-sjwcoin`` looks like this:

First, import the library and exceptions.

::

    import sjwcoinrpc
    from sjwcoinrpc.exceptions import InsufficientFunds

Then, we connect to the currently running ``sjwcoin`` instance of the current user on the local machine
with one call to
:func:`~sjwcoinrpc.connect_to_local`. This returns a :class:`~sjwcoinrpc.connection.SJWcoinConnection` objects:

::

    conn = sjwcoinrpc.connect_to_local()

Try to move one sjwcoin from account ``testaccount`` to account ``testaccount2`` using 
:func:`~sjwcoinrpc.connection.SJWcoinConnection.move`. Catch the :class:`~sjwcoinrpc.exceptions.InsufficientFunds`
exception in the case the originating account is broke:

::  

    try: 
        conn.move("testaccount", "testaccount2", 1.0)
    except InsufficientFunds,e:
        print "Account does not have enough funds available!"


Retrieve general server information with :func:`~sjwcoinrpc.connection.SJWcoinConnection.getinfo` and print some statistics:

::

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty
  

