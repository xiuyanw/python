from urllib.request import quote
import webbrowser
words=quote('hello world!!')
search='https://www.baidu.com/s?wd='+words
print(search)
webbrowser.open_new_tab(search)

#https://www.baidu.com/s?wd=hello%20world%21%21  会把空格编译成%20，把感叹号编译成%21