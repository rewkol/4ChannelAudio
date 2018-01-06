import random, wave, struct, math, time

def generate(freq, kind,  num, samples):
    toret = []

    if kind == 1:
        #White Noise
        for i in range(num):
            toret.append(struct.pack("h",int(random.uniform(-32767,32767))))
    elif kind == 2:
        #Sawtooth 
        for i in range(num): 
            osc = samples/freq
            value = 14000 * (i%osc)*(1/osc)
            toret.append(struct.pack("h",int(value)))
    elif kind == 3:
        #Sine Wave
        for i in range(num):
            value = 14000 * (math.sin(6.283*freq*(i/44100)))
            toret.append(struct.pack("h",int(value)))
    elif kind == 4:
        #Squaretooth
        for i in range(num):
            osc = samples/freq
            if (i%osc)*2<osc:
                value = 7000
            else:
                value = -7000
            toret.append(struct.pack("h",int(value)))
    
    return toret

def writes(samples):
    wav = wave.open("output.wav", 'w')
    wav.setparams((2,2,44100,samples,"NONE","not compressed"))

    remaining = samples
    while remaining > 0:
        gennum = random.randrange(5512,44101,5512)#Decides how many samples are generated per loop
        gen = generate(random.randrange(440,880,10), 4, gennum*2, samples)#Does random tones each loop. For programmed songs don't loop and write each gen out
        for byte in gen:
            wav.writeframesraw(byte)
        remaining -= gennum
        
    wav.close()

def main():
    samples = 10*44100
    writes(samples)

main()