import hashlib
import sys

def hash_fname(fname):
    m=hashlib.md5()
    with open(fname,'rb') as src_fobj:
        while True:
            data=src_fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    print(hash_fname(sys.argv[1]))