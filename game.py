print('''
            .                .                    
            :"-.          .-";                    
            |:`.`.__..__.'.';|                    
            || :-"      "-; ||                    
            :;              :;                    
            /  .==.    .==.  \                    
           :      _.--._      ;                   
           ; .--.' `--' `.--. :                   
          :   __;`      ':__   ;                  
          ;  '  '-._:;_.-'  '  :                  
          '.       `--'       .'                  
           ."-._          _.-".                   
         .'     ""------""     `.                 
        /`-                    -'\                
       /`-                      -'\               
      :`-   .'              `.   -';              
      ;    /                  \    :              
     :    :                    ;    ;             
     ;    ;                    :    :             
     ':_:.'                    '.;_;'             
        :_                      _;                
        ; "-._                -" :`-.     _.._    
        :_          ()          _;   "--::__. `.  
         \"-                  -"/`._           :  
        .-"-.                 -"-.  ""--..____.'  
       /         .__  __.         \               
      : / ,       / "" \       . \ ;          
       "-:___..--"      "--..___;-"               
                                      
      ''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure ")

direction=input("You have come to the centre of the two road!!!\n"
                "Which side would you like to go?\n 'Left' or 'Right'\n")

if direction=="Right":
    print("Game Over\nYou fell into the hole")
else:
    decision=input("Do you want to 'swim' or 'wait'?")
    if decision=="swim":
        print("Game Over\nYou were killed by the bunch of mouse Trop")
    else:
        door=input("There are three doors which are of \n"
                   "'Red' ,'Blue' and 'Yellow'!\n"
                   "Choose between these three!!!" )
        if door=="Blue":
            print("Game Over\nYou are eaten by the crocodile")
        elif door=="Red":
            print("Game Over\nYou are burened by the fire")
        else:
            print("Yayyy !!!\nYou win")
            
    
