class Solution:
    def capitalizeTitle(self, title: str) -> str:
        w=title.split()
        r=[]
        for i in w:
            if len(i)<=2:
                r.append(i.lower())
            else:
                r.append(i[0].upper()+i[1:].lower())
        return " ".join(r)