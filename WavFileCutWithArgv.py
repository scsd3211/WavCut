import sys
import NEWCutWavFile




print('Number of arguments:', len(sys.argv))

print('They are:', str(sys.argv))

print("First is ",str(sys.argv[1]))

OK  = str(sys.argv[1])

if(OK == "OKOK"):
    print("yes")

NEWCutWavFile.SetFileName(OK)

NEWCutWavFile.CutFile()


print("Run Over")