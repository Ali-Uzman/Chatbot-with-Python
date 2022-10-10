#here we are using NLK Python library which is best for Natural Language Processing Task:

from nltk.chat.util import Chat, reflections

#Pairs is the list of patterns and responses
pairs=[[r"(.*)my name is (.*)", 
       ["Hello %2, How are you today?",]
       ],
       [ r"(.*) help(.*)",
       ["I can help you.",]
       ],
       [ r"(.*) your name is?",
       ["My name is Angel, I am just Robot you can also call me Chatbot.",]
       ],
       [ r"(.*) how are you? (.*)",
       ["I am doing well", "I am Great!",]
       ],
       [ r"sorry (.*)",
       ["It's ok", "It Alright!","Never mind that!",]
       ],
       [ r"I am (.*)(good|well|okay|ok)",
       ["Nice to hear that!", "Alright Great!",]
       ],
       [ r"(hi|hello|hola|hey|holla)(.*)",
        ["Hey There", "Helo",]
       ],
       [r"what (.*) want?",
       ["Make me an offer i cannot refuse!",]
       ],
       [r"(.*) created (.*)",
       ["I am created by Uzman Ali?",]
       ],
       [r"(.*) (location|city)",
       ["Islamabad, Pakistan",]
       ],
       [r"(.*) raining in (.*)",
       ["No rain in past 2 day", " no rain here",]
       ],
       [r"how (.*) healthy (.*)",
       ["Health is very important, but i am computer so i don't have to worry",]
       ],
       [r"(.*) (sport|game|sports) (.*)",
       ["Yes, I am big fan of cricket.",]
       ],
       [r"who(.*) (cricketer|batsman)?",
       ["Waseem Akram",]
       ],
       [r"quit",
        ["Bye for now, See you soon",]
       ],
       [r"(.*)",
        ["That is nice to hear.",]
        ],
       ]

#default message at the start of program
print("Hi I am Uzman Ali. I would like to chat.Please type lower case letter to start conversations.")
#Creating Chatbot
chat= Chat(pairs, reflections)
#starting conversation
chat.converse()
