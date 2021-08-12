
# import os

# with open("infos.txt","r+") as f:
#     f.seek(0)
#     f.truncate()
# delecting the files data 



# import os
# print(os.path.abspath("newlogs.txt"))
# #got the absolute path of the file 


# import os

# var = os.getcwd()
# result = os.listdir(var)
# print(result)



# print(os.path.abspath("homework.py"))



# import os

# def soldier(path,file,format):
#     os.chdir(path)
#     i = 1
#     files = os.listdir(path)
#     with open(file) as f:
#         filelist = f.read().split("\n")

#     for file in files:
#         if file not in filelist:
#             os.rename(file,file.capitalize())


#         if os.path.splitext(file)[1] == format:
#             os.rename(file,f"{i}{format})
#             i += 1

# soldier(r"C:\Users\user\Desktop\New folder",r"J:\harrry python\runner.txt",".txt")



"""
# Akbar Op

#Exercise 9

import requests
import json

def speak(str):
       from win32com.client import Dispatch


       speak = Dispatch("SAPI.SpVoice")
       speak.Speak(str)



r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=843e0b8867404397b38554f378e8a18e", data = {"key":"value"})
var = r.content
result = json.loads(var)



speak("Welcome to the Ismail's news channel")
if __name__ == '__main__':
    for x in range(10):
        news = result["articles"][x]["description"]
        print("Today's top 10 News are: ")
        c = ("News",x+1,":",news)
        print(c)
        speak(c)
        speak("Moving on to the next news. Listen carefully")
    speak("thanks for listening")    
print("The latest news ends here")








# import requests
# import pickle 

# var = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# x = var.text
# a = x.split("\n")
# newlist = [[c] for c in a]




# file = open("exercise10","wb")
# dumped = pickle.dump(newlist,file)



# import pickle


# file = open("exercise10","rb")
# print(pickle.load(file))



# # done


"""




