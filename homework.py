import sys
class Convert:
    def __init__(self,fname):
        self.fname=fname

    def to_linux(self):
        dst_fname=self.fname+'.linux'
        with open(self.fname) as src_fobj:
            with open(dst_fname,'w') as dst_fobj:
                for line in src_fobj:
                    line=line.rstrip()+'\n'
                    dst_fobj.write(line)
        return dst_fname


    def to_windows(self):
        dst_fname=self.fname+'.doc'
        with open(self.fname) as src_fobj:
            with open(dst_fname,'w') as dst_fobj:
                for line in src_fobj:
                    line=line.rstrip()+'\r\n'
                    dst_fobj.write(line)
        return dst_fname


if __name__ == '__main__':
    a=Convert(sys.argv[1])
    a.to_linux()
    a.to_windows()
