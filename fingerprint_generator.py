import os
import re
import bs4
import codecs
import chardet
def get_dirctory():
    path = "D:\Study\gamble\\"
    names = []
    for filename in os.listdir(path):
        names += [filename]
    return names
#获取文件结构指纹
def directory_fingerprint(directory):
    root = "D:\Study\gamble\\"
    path = os.path.join(root, directory)
    pathnames = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            pathnames += [dirpath.replace(path,"").strip('\\') +filename]
    return pathnames

#获取主页内容指纹
def content_fingerprint(directory):
    result = ''
    root = "D:\Study\gamble\\"
    path = os.path.join(root, directory,'index.html')
    with codecs.open(path,"rb") as f:
        data = f.read()
        cod = chardet.detect(data)
    try:
        with open(path, 'r',encoding=cod['encoding']) as f:
            soup = bs4.BeautifulSoup(f.read(), 'html.parser')
            result += soup.title.string
            if soup.a is None:
                return result
            for parent in soup.a.parents:
                if parent is not None:
                    for content in parent.contents:
                        if "=" not in content.text:
                            result+=content.text.strip()

    except Exception as e:
        print("error")
        print(path)
        print(e)
    return result


if __name__ == '__main__':
    names = get_dirctory()
    for name in names:
        try:
            d_print = directory_fingerprint("43yyhh.com")
            c_print = print("".join([s for s in content_fingerprint(name).splitlines(True) if s.strip()]))
        except:
            print("E R R O R:"+name)
