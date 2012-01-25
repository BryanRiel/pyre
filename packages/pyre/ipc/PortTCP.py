# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import socket
# my interface
from .Port import Port


# class declaration
class PortTCP(Port):
    """
    An implementation of a process bell using a TCP port
    """


    # types
    from ..schema import inet
    from .SocketTCP import SocketTCP as tcp
    # constants
    type = socket.SOCK_STREAM


    # public data
    channel = None
    address = None

    
    # factories
    @classmethod
    def open(cls, address, **kwds):
        """
        Establish a connection to the remote process at {address}
        """
        # normalize the address
        address = cls.inet.pyre_cast(value=address)
        # create a channel
        channel = cls.tcp(address.family, cls.type, **kwds)
        # establish a connection
        channel.connect(address.value)
        # and return it
        return channel


    @classmethod
    def install(cls, address):
        """
        Attempt to acquire a port and start listening for connections
        """
        # normalize the address
        address = cls.inet.pyre_cast(value=address)
        # create the socket
        listener = cls.tcp(address.family, cls.type)
        # no need for the socket to linger in TIME_WAIT after we are done with it
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # attempt to
        try:
            # bind it to my address
            listener.bind(address.value)
        # if this fails
        except socket.error:
            # build a new address for a location chosen by the kernel
            relocated = type(address)(host=address.host, port=0)
            # bind it
            listener.bind(relocated.value)

        # find out which port we are actually able to get
        host, port = listener.getsockname()
        # and adjust the address
        address = type(address)(host=host, port=port)

        # start listening
        listener.listen(socket.SOMAXCONN)
        
        # wrap the socket up
        port = cls(channel=listener, address=address)
        # and return it
        return port


    # interface
    def close(self):
        """
        Close the port
        """
        # delegate
        return self.channel.close()


    def accept(self):
        """
        Wait until a peer process attempts to open the port and build a communication channel
        with it
        """
        # delegate
        return self.channel.accept()


    # meta methods
    def __init__(self, channel, address, **kwds):
        super().__init__(**kwds)

        self.address = address
        self.channel = channel

        return


# end of file 