"""
Given a string as input replace 1 by A, 2 by b, 3 by c and 4-9 by x. 0 and other
characters appear as it is in the new string and are not changed.
Input-> "12049brt"
Output-> Ab0xxbrt
"""

st = "12049brt"
ln = len(st)
new_str = ""
for i in range(0,ln):
  ch = st[i]
  if(ch=="1"):
    new_str = new_str + "A"
  elif(ch=="2"):
    new_str = new_str + "b"
  elif(ch=="3"):
    new_str = new_str + "c"
  elif(ch>="4" and ch<="9"):
    new_str = new_str + "x"
  else:
    new_str = new_str + ch
print(new_str)
