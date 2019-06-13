import string
import random
import nltk

#from A3
def remove_punctuation(input_string):
    
    ''' 
    Removes punctuation from input string
    
    Paramters
    ---------
    input_string: string
        input with punctuation
    
    Returns
    -------
    out_string: string 
        output without punctuation    
    '''
    
    out_string=''
    
    for char in input_string:
        if char not in string.punctuation:
            out_string=out_string+char
    
    return out_string

#from A3
def prepare_text(input_string):
    
    '''
    Takes input and makes it lowercase, removes punctuation, and puts every word in the string into a list
    
    Parameters
    ---------
    input_string: string
        input with uppercase letters, punctuation, and in one string
    
    Returns
    -------
    out_string: string 
        output without uppercase letters, punctuation, and separated   
    '''
        
    out_list=[]
    temp_string=input_string.lower() 
    temp_string=remove_punctuation(temp_string)
    out_list=temp_string.split()
    
    return out_list

#from A3
def end_chat(input_list):
    
    '''
    Checks for word 'quit' that ends the chat
    
    Parameters
    ---------
    input_string: string
        string that was typed in
    
    Returns
    -------
    output: boolean
        assigns chat equal to true or false  
    '''
    
    if 'quit' in input_list:
        output=True 
    
    else:
        output=False
    
    return output

def residency(msg):
    
    '''
    Finds word 'residency' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'residency' in msg:
        print('Enter d if you are dropping off documents, Enter t if you would like to speak with a residency deputy')
        
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg = input('INPUT :\t')
        
        if msg=='d':
            output= print ('Someone at the front counter will help you shortly')
        
        elif msg=='t':
            output= print ('A residency deputy will be out shortly')
    
            return output
    
def special_programs(msg):
    
    '''
    Finds word 'special' or 'programs' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    if 'special' in msg or 'programs' in msg:
        print ('Enter c if you are here for cross enrollment, Enter u for UC Online')
        
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
        
        if msg=='c':
            output= print ('Lora Lae will be out shortly to help you')
        
        elif msg=='u':
            output= print ('Sarah will be out shortly to help you')
        
        return output
    
def transcripts_and_verifications(msg):
    
    '''
    Finds word 'transcripts' or 'verifications' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'transcripts' in msg or 'verifications' in msg:
        print ('Enter p if you are picking up a transcript or verification,' +
        ' Enter o if you would like help with ordering a transcript or verification,' +
        ' Enter i if you are an ivnestigator')
        
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
    
        if msg=='p':
            output= print ('Please take out a photo id and someone at the front desk will help you')
    
        elif msg=='o':
            output= print ('Someone at the front desk will help you shortly with ordering')
    
        elif msg=='i':
            output= print ('Jack will be out shortly to assist you')
            
        return output

def fees(msg):
    
    '''
    Finds word 'fees' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'fees' in msg:
        print ('Enter l if want to discuss a late fee, Enter o for other')
    
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
    
        if msg=='l':
            output= print ('Please enter your PID number')
            #This creates another input box so users can type in another input after above messages asks for additional input
            msg= input('INPUT:\t')
            
        elif msg=='o':
            output= print ('Someone at the front desk will help you shortly')
            
        return output
    
def diplomas(msg):
    
    '''
    Finds word 'diplomas' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'diplomas' in msg:
        print ('Enter p if you are picking up a diploma, Enter r if you would like to order a replacement')
    
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
    
        if msg=='p':
            output= print ('Please take out a photo id and someone at the front desk will help you')
        
        elif msg=='r':
            output= print ('Someone at the front desk will help you shortly')
        
        return output
    
def pid_pac(msg):
    
    '''
    Finds word 'pid' or 'pac' in input message and prints messages.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'pid' in msg or 'pac' in msg:
        output= print ('Please take out a photo id and someone at the front desk will help you')
        
        return output
    
def scheduling(msg):
    
    '''
    Finds word 'scheduling' in input message and prints messages based on further input.
    
    Paramters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'scheduling'in msg:
        print ('All scheduling requests must be made' + 'online at least 3 business days before the room is needed' +
               ' and no exceptions are made. If you still would like to' +
               ' speak with someone please Enter o')
        
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
        
        if msg=='o':
            output= print ('Please take a seat and someone will be out shortly to speak with you')
    
        return output
    
def personal_info_updates(msg):
    
    '''
    Finds word 'personal', 'info', or 'updates' in input message and prints messages based on further input.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'personal' in msg or 'info' in msg or 'updates'in msg:
        print('Enter n for a name change request, Enter s to update social security number, Enter o for other')
        
        #This creates another input box so users can type in another input after above messages asks for additional input
        msg= input('INPUT:\t')
        
        if msg=='n':
            output= print ('Please take out the supporting documentation and someone at the front desk will help you shortly')
    
        elif msg=='o':
            output= print ('Someone at the front desk will help you shortly')
            
        elif msg=='s':
            output= print ('Please take out your signed social security card and Photo ID.' + 
                           ' Someone at the front desk will help you shortly')
            
        return output
        
def veterans_benefits(msg):
    
    '''
    Finds word 'veterans' or 'benefits' in input message and prints messages.
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'veterans' in msg or 'benefits'in msg:
        output= print ('Lisa will be out shortly to assist you')
    
        return output

def other(msg):
    
    '''
    Finds word 'other' in input message and prints messages. 
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        print output message based on msg  
    '''
    
    if 'other' in msg:
        output= print ('Someone at the front desk will assist you shortly, please take a seat while you wait')
        
        return output
    
#modified have_a_chat from A3
def registrar_chat():
    
    '''
    Chatbot prints instructions when the function is ran and then asks for an input. 
    After the first input is typed in, its prints a corresponding message. 
    This messages give further information on that topic and asks for an input based on what you need help with.  
    
    Parameters
    ---------
    msg: string
        input typed in
    
    Returns
    -------
    Return: string 
        printed output string based on msg  
    '''
    
    chat= True
    while chat:
        
        #This creates instruction message for users when they first run the function
        if chat:
            print ('Thanks for coming to the Registrars Office') 
            print ('Please type one of the following options:')
            print ('     Residency, Special Programs, Transcripts, Verifications, Fees, Diplomas')
            print ('     PID/PAC, Personal Info Updates, Veterans Benefits, or Other') 
            print('You can type quit at anytime to exit the chat')       
            chat=False
        
        #This creates an input box so users can type in one of the inputs listed in the instructions
        msg = input('INPUT :\t')
        #takes msg and takes out punctuation, makes it all lowercase, and turns msg into a list of strings 
        msg = prepare_text(msg)
        
        if end_chat(msg):
            print('Thanks for coming to the Registrars Office at UC San Diego!')
            chat = False

        elif residency(msg):
            pass
        
        elif special_programs(msg):
            pass
        
        elif transcripts_and_verifications(msg):
            pass
        
        elif fees(msg):
            pass
        
        if diplomas(msg):
            pass
        
        if pid_pac(msg):
            pass
        
        if scheduling(msg):
            pass
        
        if personal_info_updates(msg):
            pass
        
        if veterans_benefits(msg):
            pass
        
        if other(msg):
            pass
        
        