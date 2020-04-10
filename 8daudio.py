from pydub import AudioSegment
from tkinter import filedialog
from tkinter import *
from time import sleep


print("8D AUDIO CONVERTER FOR MP3s ~by WinterSoldier\n\n Contact the developer @_neural.network_ (Insta) for any help")
print("Make sure that you have 'ffmpeg' folder placed in the same directory\n\n")

# allow user input of song in mp3 from any folder on computer 
root = Tk()
root.filename =  filedialog.askopenfilename( initialdir = "/",
                                                title = "Select mp3 file to convert",
                                                filetypes = ( ( "mp3 files","*.mp3" ),( "all files","*.*" ) ) )
print(root.filename)

sound = AudioSegment.from_mp3(root.filename)



print("Type: 'normal' to use default settings or 'custom' to use your custom settings")
inp = input("")

if inp=='normal':
    adjust_jump =8
    segment_length = 200
    
elif inp=='custom':
    inp2 = input("Please input custom jump speed (INTEGER value between 2 to 20) >>>")
    adjust_jump = int(inp2)
    inp3 = input("Please input the segment length(INTEGER value between 200 to 5000) >>>")
    segment_length = int(inp3)
    
else:
    print("Wrong choice...Run Again")

_8d = sound[0]
pan_limit=[]

limit_left  = -100


for i in range(100):
    if int(limit_left) >= 100:
        break
    pan_limit.append(limit_left)
    limit_left+=adjust_jump

pan_limit.append(100)

for i in range(0,len(pan_limit)):
    pan_limit[i] = pan_limit[i] /100

print(len(pan_limit))
print(pan_limit)
print("Please wait...it may take a few seconds")
sleep(2)




c=0
flag = True


for i in range(0,len(sound)-segment_length, segment_length):

    peice = sound[i:i+segment_length]

    if c==0 and not flag:
        flag =True
        c=c+2

    if c==len(pan_limit):
        c = c-2
        flag =False

    if flag:
        panned = peice.pan(pan_limit[c])
        c+=1


    else:
        panned = peice.pan(pan_limit[c])
        c-=1

    


    _8d =_8d+panned
    print(panned)
	






print(len(_8d))
print("Writing the audio from the MEMORY to the drive")

# lets save it!
out_f = open("compiled.mp3", 'wb')

_8d.export(out_f, format='mp3')







