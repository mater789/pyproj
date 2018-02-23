import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response 三引号的形式用来输入多行文本
text_content = '''HTTP/1.x 200 OK  
Content-Type: text/html

<head>
<title>WOW</title>
</head>
<html>
<p>Wow, Python Server</p>
<IMG src="test.jpg"/>
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg','rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content.encode() + f.read()
f.close()

# Configure socket
s    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    method = request.split(' ')[0]

    # deal with GET method
    if method == 'GET':
        # ULR
        content = pic_content

        print('Connected by', addr)
        print('Request is:', request)
        conn.sendall(content)
    # close connection
    conn.close()