# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 15:09:05 2018

@author: ecupl
"""
import os,time
from win32com import client
os.chdir(r"D:/mywork/test")
#生成WORD应用程序变量
word=client.gencache.EnsureDispatch("Word.Application")
doc=word.Documents.Add()    #新建文档
word.Visible=1              #显示文档
word.DisplayAlerts=0        #显示警告
#time.sleep(6)

#DOC文件的属性和方法
range1=doc.Range(0,0)       #范围变量，前10个字符保存为range1
range1.InsertAfter("123好样的")            #加在range1的位置后面
range1.InsertAfter('加在这个位置二')       #加在先前插入文本的位置后面
range1.InsertBefore('加在最前面1')        #加在最前面的位置
range1.InsertBefore('还是在最前面2')      #继续加在最前面的位置
#os.path.dirname(__file__)   用不了，好奇怪
curr_path=os.getcwd()       #获取当前路径
doc.SaveAs(curr_path + "\\test1.doc")   #保存文件doc格式
doc.SaveAs(curr_path + "\\test1.docx")  #保存文件docx格式
doc.Close()     #关闭文件

word.Quit()     #关闭应用程序


#打开文件：第一种方法
word=client.gencache.EnsureDispatch("Word.Application")
docopen=word.Documents.Open(curr_path + "\\test1.doc","r")
#word.Visible=1    
docopen.Content
print(docopen.Content)

#打开文件：第二种方法
paras=docopen.Paragraphs
for p in paras:
    text=p.Range.Text.strip()
    print(text)
paras(2).Range.Text     #打印指定段落

#%%
#word格式设置
import os
from win32com import client
from win32com.client import constants
os.chdir("D:/mywork/test")
#创建文档
word=client.gencache.EnsureDispatch("Word.Application")
word.Visible=1
word.DisplayAlerts=0
doc = word.Documents.Add()
range1=doc.Range(0,0)
range1.InsertAfter("这是加的第一行字\n\n这是加的第二行字\n")
range1.InsertAfter("这是第三行\n这是第四行\n")
range1.InsertBefore("————加个副标题\n")
range1.InsertBefore("这是个正式标题\n")
currpath = os.getcwd()
doc.SaveAs(currpath+"\\word\\study.docx")

#格式调整
#doc.Content()
#print(doc.Content)
#还是不行，就不用这个方法了吧！

paras=doc.Paragraphs
for i in paras:
    print(i.Range.Text.strip())     #打印清除格式的doc

#设置主标题
para_range1 = paras(1).Range        #选中段落1
para_range1.Style = constants.wdStyleHeading1       #设置标题格式
para_range1.ParagraphFormat.Alignment = constants.wdAlignParagraphCenter    #居中对齐
para_range1.Style.Font.Name = "微软雅黑"         #设置字体格式

#设置副标题
para_range2 = paras(2).Range
para_range2.Style = constants.wdStyleHeading3
para_range2.ParagraphFormat.Alignment = constants.wdAlignParagraphRight     #右对齐
para_range2.Style.Font.Name = "微软雅黑"        #设置字体格式
para_range2.Style.Font.Color = 0x0000ff        #设置字体颜色,只能选十六进制,大小写不一样

#设置具体内容
para_range3 = paras(3).Range
para_range3.Style.Font.Bold = 0;     #加粗
para_range3.Style.Font.Italic = 1;   #斜体
para_range3.Style.Font.Underline = 1; #加底线
para_range6 = paras(6).Range
para_range6.Style.Font.Shadow = 0      #加阴影
para_range6.Style.Font.Outline = 1      #加外框
#para_range6.ParagraphFormat.Alignment = constants.wdAlignParagraphCenter  #居中对齐
para_range6.Font.Size = 15      #字体大小

#%%加入表格
para_range4 = paras(4).Range
table = doc.Tables.Add(para_range4,3,4)
data = [[11,12,13,14],
        [21,22,23,24],
        [31,32,33,34]]
for i in range(1,table.Rows.Count+1):
    for j in range(1,table.Columns.Count+1):
        #添加文字
        table.Cell(i,j).Range.Text = data[i-1][j-1]
table.Cell(2,2).Range.Font.Color = 0XFF0000     #表格字体颜色
table.Cell(2,2).Range.Font.Bold = 1             #表格字体加粗


#%%
#加入图片
para_range7 = paras(16).Range
para_range7.InlineShapes.AddPicture(r"D:\mywork\test\images\tooopen_sl_241297083966.jpg",False,True)


#%%
#清除源字符及目标字符的格式
word.Selection.Find.ClearFormatting()
word.Selection.Find.Replacement.ClearFormatting()

#全部替换
word.Selection.Find.Execute("这是",False,False,False,False,False,True,constants.wdFindContinue,
                          False,"This is",constants.wdReplaceAll)

#全部替换
word.Selection.Find.Execute("This is",False,False,False,False,False,False,constants.wdFindContinue,
                          False,"这是",constants.wdReplaceOne)

#%%
#关闭
doc.Close()
word.Quit()

#%%多文件替换
import os
from win32com import client
from win32com.client import constants
os.chdir("D:\\mywork\\test")
word = client.gencache.EnsureDispatch("Word.Application")
word.Visible = 0
word.DisplayAlerts = 0
runpath = os.getcwd() + "\\word"

#将doc或者docx文件写入列表
trees = os.walk(runpath)
allfiles = []
for dirname, subdir, files in trees:
    print(dirname)
    print(subdir)
    print(files)
    print("\n")
    for file in files:
        ext = file.split(".")[-1]
        if ext=="doc" or ext=="docx":
            allfiles.append(dirname+"\\"+file)

#对文件进行批量替换
if len(allfiles) > 0 :
    for dfile in allfiles:
        print(dfile)
        #打开文件
        doc = word.Documents.Open(dfile)
        #清楚搜索和替换文字的格式
        word.Selection.Find.ClearFormatting()
        word.Selection.Find.Replacement.ClearFormatting()
        #进行替换
        word.Selection.Find.Execute("学习",False,False,False,False,False,True,constants.wdFindContinue,
                          False,"study_test",constants.wdReplaceAll)
        doc.Close()

word.Quit()

























