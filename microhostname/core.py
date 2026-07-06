import socket

def show():

    print()
    print("MicroHostname")
    print("="*40)

    print("Hostname :", socket.gethostname())
    print("FQDN     :", socket.getfqdn())

    try:
        print("Local IP :", socket.gethostbyname(socket.gethostname()))
    except Exception as e:
        print(e)
