import os
class Convert:
    def __init__(self,fname):
        self.fname=fname

    def to_linux(self):
        dst_fname=os.path.splitext(self.fname)[0]+'.linux'
        with open(self.fname,'r') as src_fobj:
            with open(dst_fname,'w') as dst_fobj:
                for line in src_fobj:
                    line=line.rstrip()+'\n'
                    dst_fobj.write(line)
        return dst_fname



    def to_windows(self):
        dst_fname=os.path.splitext(self.fname)[0]+'.doc'
        with open(self.fname,'r') as src_fobj:
            with open(dst_fname,'w') as dst_fobj:
                for line in src_fobj:
                    line=line.rstrip()+"\r\n"
                    dst_fobj.write(line)

        return dst_fname


if __name__ == '__main__':
    c=Convert('/tmp/passwd')
    c.to_linux()
    c.to_windows()

