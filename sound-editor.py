import os
from pydub import AudioSegment


def chopAudio(song_name, desired_start_time,desired_end_t):
    desired_start_time *= 1000
    desired_end_t *= 1000

    if song_name[-3:] == "mp3":
        song = AudioSegment.from_mp3(song_name)

        choppedSong = song[desired_start_time:-desired_end_t]

        choppedSong.export("chopped-"+song_name, format = "mp3")
        print("'chopped-"+song_name+"' has been saved to your Directory!")
    
    elif song_name[-3:] == "wav":
        song = AudioSegment.from_wav(song_name)

        choppedSong = song[desired_start_time:-desired_end_t]

        choppedSong.export("chopped-"+song_name, format = "wav")
        print("'chopped-"+song_name+"' has been saved to your Directory!")
    else:
        print("Incompatible file type. Convert your file to either .wav or .mp3 to work with this software!")
    
    
def changeDB(song_name,db_change):
    song = AudioSegment.from_mp3(song_name)
    song += db_change
    if song_name[-3:] == "mp3":
        song.export("adjustedVolume-"+song_name, format = "mp3")
        print("'chopped-"+song_name+"' has been saved to your Directory!")
    elif song_name[-3:] == "wav":
        song.export("adjustedVolume-"+song_name, format = "wav")
        print("'chopped-"+song_name+"' has been saved to your Directory!")
    else:
        print("Incompatible file type. Convert your file to either .wav or .mp3 to work with this software!")



def main(): 
    #get user input
    inputSong = input("Enter the file name of your song:")

    beginningCutoff = input("How many seconds into the beginning of the file would you like to remove?")
    endCutoff = input("How many seconds at the end of the file would you like to remove?")

    #convert string to int
    beginningCutoff = int(beginningCutoff)
    endCutoff = int(endCutoff)

    #call chopAudio
    chopAudio(inputSong,beginningCutoff,endCutoff)


# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main()
