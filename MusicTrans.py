import re

def translate(string):
    try:
        bpm = eval(string[:string.find("::")])
    except:
        return "ERROR:bpm"
    music = string[string.find("::")+2:string.rfind("::")]
    s = 2646000/bpm#@44100 samples/sec
    
    notes = {"__":0,"A0":27.5,"A#0":29.1352,"Bb0":29.1352,"B0":30.8677,"Cb1":30.8677,"C1":32.7032,"B#0":32.7032,"C#1":34.6478,"Db1":34.6478,"D1":36.7081}
    #Incomplete lists as this is a POC
    times = {"1/32":s*0.03125,"1/16":s*0.0625,"1/8":s*0.125,"1/4":s*0.25,"1/2":s*0.5,"0":0,"1":s*1,"1.5":s*1.5,"2":s*2,"3":s*3,"4":s*4,"5":s*5,"6":s*6,"7":s*7,"8":s*8}

    pat = re.compile("(\\([0-9/]+:[A-G0-9b#_]{2,3}\\))")
    out = ""
    match = pat.match(music)
    while match is not None:
        #Parse first match
        parse = match.group(1)
        out+= str(times.get(parse[1:parse.find(":")]))+" Samples @ "+str(notes.get(parse[parse.find(":")+1:-1]))+" Hz\n"
        #Remove from string
        music = music[len(parse):]
        match = pat.match(music)
    
    return out

def main():
    string = input()
    print(translate(string))
    
main()
