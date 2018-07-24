import tarfile
# tar=tarfile.open('/tmp/demo.tar.gz',"w:gz")
# tar.add('/etc/passwd')
# tar.add('/etc/resolv.conf')
# tar.close()


tar1=tarfile.open('/tmp/demo.tar.gz')
tar1.extractall(path='/tmp')
tar1.close()