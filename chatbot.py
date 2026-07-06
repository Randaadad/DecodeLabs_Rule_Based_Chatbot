answers = {
    "hello" : "Hello!" ,
    "hi" : "Hi!" ,
    "hey" : "hello buddy!",
    "how are you" : "i'm doing great",
    "help" : "what can i do for you ?",
    "what can you do " : "i can answer simple questions" ,
    "thank you" : "you're welcome" , 
    "tell me a joke" :"Why do programmers prefer dark mode? Because light attracts bugs!",
    "what is your name ?" : "my name is MyBot" ,
    "what can  you do ?" : "i respond to greetings and small talk",
    "sorry!" : "no worries at all!"
}
exitlines = {"bye" , "exit"}
print ("MyBot : Hello! I'm a rule bases chatbot. Type 'bye' to exit")
while True :
    user_input_text = input("You :")
    clean_input = user_input_text.lower().strip()
    if clean_input in exitlines :
        print ("MyBot : Goodbye!")
        break
    reply = answers.get(clean_input , "i dont understand your question , type 'help'.")
    print("MyBot :" , reply)