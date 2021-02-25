import time
import requests
#1 = long
#0 = short
letters = ["a:0 1","b:1 0 0 0","c:1 0 1 0","d:1 0 0","e:0","f:0 0 1 0","g:1 1 0",
           "h:0 0 0 0","i:0 0","j:0 1 1 1","k:1 0 1","l:0 1 0 0","m:1 1","n:1 0",
           "o:1 1 1","p:0 1 1 0","q:1 1 0 1","r:1 0 1","s:1 1 1","t:1","u:0 0 1",
           "v:0 0 0 1","w:0 1 1","x:1 0 0 1","y:1 0 1 1","z:1 1 0 0"]
index = 0
morse = []
substrings = []
delay_short = 1
delay_long = 2
ret = None
url = "http://142.250.185.163:80"
def main():
    while True:
        text = input("Enter sentence (enter exit to leave): ").lower()
        #adding an exit-condition
        if (text=="exit"):
            break
        for char in text:
            #finding the correct letter
            for item in letters:
                if char in item:
                    index = letters.index(item)
                    print(letters[index])
                    substrings = letters[index].split(":")
                    morse = substrings[1].split()
                    #print(morse)

                    for element in morse:
                        if (element=="0"):
                            #on
                            ret = requests.get(url+"/input?value=100")
                            time.sleep(delay_short)
                            #off
                            ret = requests.get(url+"/input?value=0")
                            print(ret.text)
                        elif (element=="1"):
                            test = 3
                            #on
                            ret = requests.get(url+"/input?value=100")
                            time.sleep(delay_long)
                            #off
                            ret = requests.get(url+"/input?value=0")
                            print(ret.text)
                        print(element)
            #adding "blank" for readability
            time.sleep(delay_short)
            print("\n")
        print("\n")

main()
