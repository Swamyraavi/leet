class Solution:
    def scoreOfString(self, s: str) -> int:
      n=len(s)
      d=[*s]
      c=[] 
      for i in range(0,n):
        c.append(d[i])
      z=0
      for i in range(0,len(c)-1):
        s=abs(ord(c[i])-ord(c[i+1]))
        z=z+s
      return z