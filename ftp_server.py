import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 80
server = 'pythonprogramming.net'
server_ip = socket.gethostbyname(server)
print(server_ip)

## Random tests to get a feel for it
def main():

    request = "GET / HTTP/1.1\nHost: "+server+"\n\n"

    s.connect((server, port))
    s.send(request.encode())
    result = s.recv(4096)

    # Print the site
    while( len(result) > 0):
        print(result)
        result = s.recv(4096)
    
    for x in range(1,23):
        if pscan(x):
            print("Port {} is open!!!!".format(x))
        else:
            print("Port {} is closed.".format(x))
    

def pscan(scan_port):
    try:
        s.connect((server, scan_port))
        return True
    except:
        return False

if __name__ == "__main__":
    main()