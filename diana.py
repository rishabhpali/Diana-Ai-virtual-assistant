import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from email.message import EmailMessage
import pyautogui
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import time as tt
from nltk.tokenize import word_tokenize

from newvoices import speak
import openai
openai.api_key = "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"





sender = 'diana.for.rishabh@gmail.com'
epwd = 'hyzunleyybwkgouq'
phone_no = '+91 89202 08655'
#to = 'rishabhp780@gmail.com'

#engine = pyttsx3.init()

#def speak(text):
 #   engine.say(text)
  #  engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")#HOUR = I, MIN = M,SECOND = S
    speak("let me check....hmmmmmmm....the time is : ")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("today's date is : ")
    speak(date)
    speak(month)
    speak(year)
    
def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("A very good and pleasent morning to you!")
    elif hour >= 12 and hour <18:
        speak("a very good afternoon to you!")
    elif hour >= 18 and hour < 24:
        speak("Good and pleasant evening to you!")
    else:
        speak("relaxing and peaceful night to you!")
 
def wishme():
    speak("Nice to have you back ! ")
    greeting()
    speak("how can i help you?")
def takeCommandCMD():
    query = input("ask me anything you want to know...\n")
    return query

def takeCommandMIC():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmm.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(query)
    
    except Exception as e:
        print(e)
        speak("can you please repeat that?....")
        return "none"
    return query

def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, epwd)
    email = EmailMessage()
    email['From'] = sender
    email['to'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()
    
def sendwhatsmsg(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no +'&text='+Message)
    sleep(10)
    pyautogui.press('enter')
def searchgoogle():
    speak('what do you want to search in google ?')
    search = takeCommandMIC()
    wb.open('https://www.google.com/search?q='+search)
def news():
    newsapi = NewsApiClient(api_key='5e2527c963de439886c13e53d391706b')
    speak('what topic you need the news about ?')
    topic = takeCommandMIC()
    data = newsapi.get_top_headlines(q=topic,
                                     language='en',
                                     page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
        
    speak("thats it for now. i will update more in some time")
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)
def screenshot():
    name_img = (tt.time())
    name_img = f'C:\\Users\\Asus\\OneDrive\\Desktop\\assistant\\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()
start_sequence = "\nAI:"
restart_sequence = "\nHuman:"

prompt = "the following is a conversation with an AI assistant."
def gpt_output(prompt):
    response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    temperature=0.9,
    max_tokens = 150,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0.6,
    stop = ["Human:", "AI:"]
    )  
    data = response.choices[0].text
    print(data)
    speak(data)
       
    
    
#https://api.openweathermap.org/data/2.5/weather?q={New Delhi}&units=imperial&appid={d63aee3e9700c501e1ea0663cc3d601b}

if __name__ == "__main__":
    wishme()
    wakeword = "diana"
    while True:
        query = takeCommandMIC().lower()
        query1 = query
        query = word_tokenize(query)
        print(query)
        if wakeword in query:
            if'time' in query:
                time()
            elif 'date' in query:
                date()
            elif 'mail' in query:
                email_list = {
                    'test': 'rishabhp780@gmail.com' 
                }
                try:
                    speak("to whom you want to send the mail ?")
                    name = takeCommandMIC()
                    reciever = email_list[name]
                    speak("what's the subject of the mail ?")
                    subject = takeCommandMIC()
                    speak('what should i say ?')
                    content = takeCommandMIC()
                    sendEmail(reciever, subject, content)
                    speak("i have sent the mail")
                except Exception as e:
                    print(e)
                    speak("unable to send the email")
            elif 'whatsapp' in query:
                user_name = {
                    'Diana': '+91 99200 53111'
                }
                try:
                    speak("to whom you want to send the mail ?")
                    name = takeCommandMIC()
                    reciever = user_name[name]
                    speak("what's the message ?")
                    message = takeCommandMIC()
                    sendwhatsmsg(phone_no, message)
                    speak("i have sent the message")
                except Exception as e:
                    print(e)
                    speak("unable to send the message")
            elif 'wikipedia' in query:
                speak('searching on wikipedia....')
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences = 4)
                print(result)
                speak(result) 
            elif 'search' in query:
                searchgoogle()  
            elif 'youtube' in query:
                speak("what should i search on youtube ?")
                topic = takeCommandMIC()
                pywhatkit.playonyt(topic)
            elif 'news' in query:
                news()
            elif 'read' in query:
                text2speech()
            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('open','')))
            elif 'joke' in query:
                speak(pyjokes.get_joke())
            elif 'screenshot' in query:
                screenshot()
            elif 'remember' in query:
                speak("i am pretty intellingent for that. now tell me?")
                data = takeCommandMIC()
                speak("you said me to remember that"+data)
                remember = open('data.txt','w')
                remember.write(data)
                remember.close()
            elif 'do you know anything' in query:
                remember = open('data.txt','r')
                speak("you told me to remember that"+remember.read())
                
            elif 'offline' in query:
                speak('have a nice day. Thanks for interacting with me')
                quit()
            else:
                gpt_output(query1)
            
    
    
