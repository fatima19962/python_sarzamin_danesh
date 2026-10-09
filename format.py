def changePosition(text,len,position,symbol=' '):
    if position>len or position<0:
        return "Error"
    else:
        text=text[:position]+symbol+text[position+1:]
        return text
    

print(changePosition("HelloWorld",10,4,'-'))  # Hell-World
print(changePosition("HelloWorld",10,11,'-'))  # Error
print(changePosition("HelloWorld",10,-1,'-'))  # Error  