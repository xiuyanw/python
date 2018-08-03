import sys
class Covert:
    def __init__(self,fname):
        self.fname=fname

    def to_Linux(self):
        dst_name=self.fname+".linux"
        with open(self.fname) as src_fobj:
            with open(dst_name,'w') as dst_fobj:
                while True:
                    for line in src_fobj:
                        if not line:
                            break
                        line=line.strip()+'\n'
                        dst_fobj.writelines(line)
    def to_windows(self):
        dst_name=self.fname+".windows"
        with open(self.fname) as src_fobj:
            with open(dst_name,'w') as dst_fobj:
                while True:
                    for line in src_fobj:
                        if not line:
                            break
                        line=line.strip()+'\r\n'
                        dst_fobj.writelines(line)

if __name__ == '__main__':
    a=Covert(sys.argv[1])
    a.to_Linux()
    a.to_windows()