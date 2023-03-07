import os
import time


tries = 3
password = input("\n type your password : \t")


while tries>0:

    tries-=1

    
    
    if (password == 'pass' and tries!=0):

        print('Login successfull')

        break




    if(password != 'pass'):

        print(f'\n {tries+1} tries left')

        print('\n Wrong password try again')

        

        password = input("\n type your password : \t")




    if(tries == 0):


        print('\nLogin Failed')

        print(f'You have {tries} tries left, Database and server has been transferred to secure server. Good Bye...')


        print('\n \n Self-destruction mode activated , App will be destroyed in 5 sec')
         
        i = 5
        
        while i>=0:

            i-=1

            time.sleep(1)

            print(i)

            if(i == 0):
                os.remove('self-destruction.py')

