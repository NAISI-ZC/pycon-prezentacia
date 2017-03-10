`robotremoteserver.py` is implementing the xml-rpc. It's open source library.
You can check it out here: https://github.com/robotframework/PythonRemoteServer

This library takes instance of our library as argument, also with ip and port
on which it will be listening for xml calls.

Create some virtual machine and copy `remote_coffee_library` on this "remote
server" and run with python. It will open port and starts listening for calls.

