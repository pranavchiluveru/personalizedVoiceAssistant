from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import json
import time
import wikipedia
import datetime

def talkToMe(audio):
     print(audio)
     tts= gTTS(text=audio,lang='en')
     tts.save('audio.mp3')
     os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def text_processing(text):
    stopwords = ["what","is","according","weather","hey","hi","to","wikipedia","search","please",
    "play","today","today's","which","day's","as","per","the","in","temperature","humidity"]
    for i in stopwords:
        text = text.replace(i,'')
    return text.strip()

def greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talkToMe("Good Morning!")
    elif hour>=12 and hour<18:
        talkToMe("Good Afternoon!")
    else:
        talkToMe("Good Evening!")


def calendar(temp):
    dic = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thurday',4:'Friday',5:'Saturday',6:'Sunday'}
    talkToMe("Today is "+ dic[temp])


def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain+'.com/'
            webbrowser.open(url)
            print('Done!')
        else:
            pass


    elif 'date' in command:
        strdate = datetime.datetime.now().strftime("%d %m %Y")
        talkToMe("Today's date is "+strdate)

    elif 'day' in command:
        temp = datetime.datetime.today().weekday()
        calendar(temp)

    elif 'year' in command or 'yer' in command:
        talkToMe("This is" + str(datetime.datetime.now().year))

    elif 'time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        talkToMe("The time is "+strTime)
    
    elif 'wikipedia' in command:
        talkToMe("what are you searching for")
        q=myCommand()
        talkToMe("searching for " + q)
        talkToMe(wikipedia.summary(q,
                                      sentences = 3))


    elif 'greeting' in command:
        talkToMe('hello ')
        greetings()

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'weather forecast in ' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            base_url = "http://api.openweathermap.org/data/2.5/weather?appid=b14cfb87644c1d34d3518a1693391e06&q="
            complete_url = base_url + city
            response = requests.get(complete_url)
            time.sleep(0.5)
            x = response.json()
            if x["cod"] != "404":
                 y = x["main"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talkToMe("It is " + weather_description)

    elif 'temperature in ' in command:
        reg_ex = re.search('temperature in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            base_url = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            complete_url = base_url + city
            response = requests.get(complete_url)
            time.sleep(0.5)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
            current_temperature = y["temp"]
            talkToMe("The current temperature in " + city + "is " + str(current_temperature-273.15))
    
    elif 'humidity in ' in command:
        reg_ex = re.search('humidity in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            base_url = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
            complete_url = base_url + city
            response = requests.get(complete_url)
            time.sleep(0.5)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
            current_humidiy = y["humidity"]
            talkToMe("The current humidity is " + str(current_humidiy))



    elif 'gmail' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'chaitu' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('pranav.chiluveru@gmail.com', 'pranavchiluveru99')

            #send message
            mail.sendmail('pranav.chiluveru@gmail.com', 'ck99rox@gmail.com', content)

        
        elif 'pranav' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('pranav.chiluveru@gmail.com', 'xyz')

             #send message
            mail.sendmail('pranav.chiluveru@gmail.com', 'pk99rox@gmail.com', content)



        elif 'dhanush' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('pranav.chiluveru@gmail.com', 'pranavchiluveru99')
            
             #send message
            mail.sendmail('pranav.chiluveru@gmail.com', 'shivadhanushm2598@gmail.com',content)


        else:
            talkToMe('I don\'t know what you mean!')


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
