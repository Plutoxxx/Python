import paramiko

transport = paramiko.Transport(('192.168.146.128', 22))
transport.connect(username='root', password='13222')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('笔记本', '/tmp/test_yang')
# 将remove_path 下载到本地 local_path
sftp.get('/root/oldboy.txt', 'linux.txt')

transport.close()