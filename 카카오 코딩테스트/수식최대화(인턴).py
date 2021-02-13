import itertools

def cal(e,k):
    h=e.split(k[0])
    
    for i in h:
        if len(k)<=2:
            del(k[0])    
            h[h.index(i)]=cal(i,k[0])
     
    print(h)
    for i in h:
        if i==h[0]: 
            c=eval(h[0])
            continue
        if k[0]=='-': c-=eval(i)
        elif k[0]=='+': c+=eval(i)
        elif k[0]=='*': c*=eval(i)
        print(c)
       
      
    return c

def solution(expression):
    k=['*','+','-']
    imp=list(itertools.permutations(k,3))
    answer = 0
    for r in imp:
        if answer <=abs(cal(expression, r)):
            answer=abs(cal(expression, r))
    return answer

a= solution("100-200*300-500+20")