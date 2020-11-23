def busqueda(f,x0,dx,n):
    xant=x0
    xact=xant+dx
    fant=expEval(f,xant)
    fact=expEval(f,xact)
    cont=1
    while cont<n:
        xant=xact
        xact=xant+dx
        fant=expEval(f,xant)
        fact=expEval(f,xact)
        
        if fant*fact<0:
            print("Hay una raiz de f en: ","[ ",xant," , ",xact," ]")
        cont+=1