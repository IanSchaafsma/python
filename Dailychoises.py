while True:
    print("welkom bij daily choises")
    Start = input("Wil je beginnen ja/nee ")
    if Start == 'ja':
     print("Veel plezier!")
    elif Start == 'nee':
     print("Ok doei")
     break     
    
    print("Je wekker gaat af wat doe je?")
    Vraag1 = input("A = je snoozed je wekker nog 5 minuutjes B = ja staat op ")
    if Vraag1 == 'A':
     print("je word wakker en shit je bent nu al dik een uur te laat")
    elif Vraag1 == 'B':
     print("je pakt je spullen en stapt de deur uit")   
    
    print("pak je je fiets of ga je lopen")
    Vraag2 = input("fiets/lopen ")
    if Vraag2 == 'fiets':
     print("je pakt je fiets en gaat naar het station")
    elif Vraag2 == 'lopen':
     print("je begint met lopen naar het station")   

    print("je staat op het station neem je koffie of thee")
    Vraag3 = input("koffie/thee ")
    if Vraag3 == 'koffie':
     print("mhm wat een lekker bakkie koffie")
    elif Vraag3 == 'thee':
     print("mhm wat een lekker koppie thee")   

     print("je pakt je trein ga je staan of zitten")
    Vraag4 = input("staan/zitten ")
    if Vraag4 == 'staan':
     print("pff wel vermoeiden hoor")
     break
    elif Vraag4 == 'zitten':
     print("even lekker zitten")
     break 
    
    else: print("je bent klaar")
