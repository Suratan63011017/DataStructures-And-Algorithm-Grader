'''
กฤษฎากำลังอ่านหนังสืออิเล็กทรอนิกส์เพื่อเตรียมสอบอยู่ในห้องสมุดของโรงเรียนชื่อดังประจำจังหวัดแห่งหนึ่ง
แล้วก็มีความคิดผุดหนึ่งขึ้นมาในหัวของกฤษฎา ถ้าหากสามารถ Auto Highlight คำที่ต้องการจาก Text ได้ก็คงจะดีไม่น้อย
แต่กฤษฎาไม่รู้จะทำอย่างไรดี กฤษฎาจึงอยากจะไหว้วานคุณให้ช่วยเขียนโปรแกรมในการ Highlight Text แบบที่กฤษฎาต้องการ
'''
print("*** Reading E-Book ***")
txt,highlight = input("Text , Highlight : ").split(",")
for i in range(len(txt)):
    if txt[i]==highlight:
        print("[{0}]".format(txt[i]),end="")
    else:
        print(txt[i],end="")