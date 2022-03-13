import os
import time
import subprocess
import data_query
import eventlet
# 源码
def system(*args, **kwargs): # real signature unknown
    """ Execute the command in a subshell. """
    urls = data_query.get_url()
    count = 0
    i = 0
    print(len(urls))
    for url in urls:
        if i < 100:
            i+=1
            continue
        i+=1
        print("number:"+str(i))
        domain = url[0].replace("\n","")
        dir = "D:\Study\gamble\\"+url[0].replace("/","").replace("http:","").replace("https:","").replace("\n","")

        p = subprocess.Popen("wget -nH -m -P "+dir+" "+domain)
        time.sleep(60)
        p.kill()

        count+=1
        # if count == 20:
        #     break
    pass
if __name__ == '__main__':
    system()
