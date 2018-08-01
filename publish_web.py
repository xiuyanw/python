import requests
from urllib.request import urlopen
import hashlib
import os
import tarfile


def get_pack_name(version):
    version_url = "http://192.168.1.173/deploy/%s_version" % version
    r = requests.get(version_url)
    r.encoding = 'utf8'
    ver = r.text.strip()
    pack_url = "http://192.168.1.173/deploy/packages/wpress_%s.tar.gz" % ver
    return pack_url


def download(url):
    html = urlopen(url)
    fname = url.split('/')[-1]
    fname = os.path.join('/var/tmp', fname)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(4096)
            if not data:
                break
            fobj.write(data)
    html.close()
    return fname


def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as src_fobj:
        while True:
            data = src_fobj.read(4096)
            if not data:
                break
            m.update(data)
        return m.hexdigest()


def check_pack(fname):
    local_md5 = check_md5(fname)
    local_name = os.path.basename(fname)
    url = 'http://192.168.1.173/deploy/packages/' + local_name + '.md5'
    remote_md5 = requests.get(url).text.strip()
    if local_md5 == remote_md5:
        return True
    return False


def deploy(fname):
    web_root = "/var/www"
    os.chdir(web_root)
    tar = tarfile.open(fname, 'r:gz')
    tar.extractall()
    tar.close()
    dst_fname = fname.replace('.tar.gz', '')
    dst_fname = os.path.basename(dst_fname)
    dst_fname = os.path.join(web_root, dst_fname)
    link = '/var/www/html/wordpress'
    if os.path.islink(link):
        os.unlink(link)
    os.symlink(dst_fname, link)


if __name__ == '__main__':
    prompt = """(0) 最新版本
(1) 上一个版本
请选择(0/1): """
    choice = input(prompt)
    if choice == '0':
        version = 'live'
    elif choice == '1':
        version = 'last'
    url = get_pack_name(version)
    print(url)
    fname = download(url)
    print(fname)
    fileok = check_pack(fname)
    if fileok:
        deploy(fname)
    else:
        print("下载的文件已损坏，请重新下载！！")
