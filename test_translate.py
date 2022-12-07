# utf-8
import os
from translate import Translator

translator = Translator(from_lang="zh", to_lang="en")
Chinese_prompt = input("请输入中文提示词\n")
translation = translator.translate(Chinese_prompt)
print("您输入的提示词被翻译为：" + translation + "\n")
command = 'python scripts/txt2img.py --prompt "' + translation + '" --plms'
print("执行代码： " + command + "\n")
os.system(command)
