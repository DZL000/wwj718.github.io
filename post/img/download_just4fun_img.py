'''
cd /Users/wuwenjie/just4funhugo/quickstart/content/post
ack -ho "http:[^\(\)\[\]]*?\.(png|jpg|jpeg|gif)" > /tmp/just4fun_img_list.txt
取得图片列表保存下来
'''

import subprocess
with open("/tmp/just4fun_img_list.txt") as png_url_list:
    urls = set(png_url_list.readlines()) # 去重
    # print(len(urls))
for url in urls: 
    if "just4fun" in url:
        cmd = f"wget {url}"
        # print(url)
        subprocess.call(cmd,shell=True) # error timeout
    else:
        print(url)
