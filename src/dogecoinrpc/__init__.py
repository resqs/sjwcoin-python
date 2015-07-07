# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
sjwcoin-python - Easy-to-use SJWcoin API client
"""


def connect_to_local(filename=None):
    """
    Connect to default sjwcoin instance owned by this user, on this machine.

    Returns a :class:`~sjwcoinrpc.connection.SJWcoinConnection` object.

    Arguments:

        - `filename`: Path to a configuration file in a non-standard location (optional)
    """
    from sjwcoinrpc.connection import SJWcoinConnection
    from sjwcoinrpc.config import read_default_config

    cfg = read_default_config(filename)
    if cfg is None:
        cfg = {}
    #port = int(cfg.get('rpcport', '18332' if cfg.get('testnet') else '19965'))
    port = int(cfg.get('rpcport', '19965'))
    rpcuser = cfg.get('rpcuser', '')
    rpcpassword = cfg.get('rpcpassword', '')

    return SJWcoinConnection(rpcuser, rpcpassword, 'localhost', port)


def connect_to_remote(user, password, host='localhost', port=19965,
                      use_https=False):
    """
    Connect to remote or alternative local sjwcoin client instance.

    Returns a :class:`~sjwcoinrpc.connection.SJWcoinConnection` object.
    """
    from sjwcoinrpc.connection import SJWcoinConnection

    return SJWcoinConnection(user, password, host, port, use_https)
