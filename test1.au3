;第一步:聚焦另存为窗口,title:另存为,"text",controlId:写ID可以识别
ControlFocus("请输入要保存的文件名…","text","40965")
;暂停脚本的执行直至指定窗口存在（出现）为止
WinWait("[CLASS:#32770]","",10)
Sleep(2000)
$var=ControlGetText("请输入要保存的文件名…","","Edit1")
global $AYYAY = StringSplit($var,'.');
$path=$CmdLine[1]&"."&$AYYAY[2]
;第二步:填充文件名地址,其中$CmdLine[1]代表exe执行时的动态参数,
;例如 kuang.exe "D:/test/a.html",这样就可以动态改变地址的名字，通过python
ControlSetText("请输入要保存的文件名…","","Edit1",$path)
;延时函数
Sleep(2000)
;第三步:点击保存按钮,进行下载,title:另存为,"text"写成空,controlId:写成Button2（ClassnameNN）也可以识别
ControlClick("请输入要保存的文件名…","","Button2")