;��һ��:�۽����Ϊ����,title:���Ϊ,"text",controlId:дID����ʶ��
ControlFocus("������Ҫ������ļ�����","text","40965")
;��ͣ�ű���ִ��ֱ��ָ�����ڴ��ڣ����֣�Ϊֹ
WinWait("[CLASS:#32770]","",10)
Sleep(2000)
$var=ControlGetText("������Ҫ������ļ�����","","Edit1")
global $AYYAY = StringSplit($var,'.');
$path=$CmdLine[1]&"."&$AYYAY[2]
;�ڶ���:����ļ�����ַ,����$CmdLine[1]����exeִ��ʱ�Ķ�̬����,
;���� kuang.exe "D:/test/a.html",�����Ϳ��Զ�̬�ı��ַ�����֣�ͨ��python
ControlSetText("������Ҫ������ļ�����","","Edit1",$path)
;��ʱ����
Sleep(2000)
;������:������水ť,��������,title:���Ϊ,"text"д�ɿ�,controlId:д��Button2��ClassnameNN��Ҳ����ʶ��
ControlClick("������Ҫ������ļ�����","","Button2")