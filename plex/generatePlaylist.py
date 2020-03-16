import os
import sys
import random
import moviepy.editor as mp
import time
import math
from datetime import datetime, timedelta

# Display help
# Check if it is a backup file
backup = False
if not len(sys.argv) > 1:
    print ("Incorrect Usage: python3 generateShowList.py <backup? (yes | no)>")
    exit()
else:
    if sys.argv[1] == "yes":
        backup = True
        print ("BACKUP FLAG WAS SET TO TRUE")
        time.sleep(3)
if dir == "":
    print ("Please populate your 'dir' variable! It cannot be null. Open up the script")
    exit()


########################################################
########################################################
#        Edit these variable to your system!           #
########################################################
########################################################

cartoons = ["1973 Super Friends", "1977 The All-New Super Friends Hour", "1978 Challenge of the SuperFriends", "1979 The World's Greatest Super Friends",
            "1984 Super Friends The Legendary Super Powers Show", "1985 The Super Powers Team Galactic Guardians", "A Pup Named Scooby Doo", "Baby Looney Tunes", "Courage The Cowardly Dog",
            "Dexter's Laboratory", "Ed,Edd n' Eddy", "Josie and the Pussycats", "Popeye", "Scooby Doo, Where Are You", "Speed Buggy", "SuperFriends(1980)", "The 13 Ghosts Of Scooby-Doo",
            "The Flintstones", "The Jetsons", "The Looney Tunes Show", "The New Scooby-Doo Movies", "The Pink Panther Cartoon", "The Smurfs",
            "Tom & Jerry"]

dir = "/mnt/plexNAS/TV/" # Directory to grab shows from (make sure there is a "/" at the end!)
tvDirectory = "/mnt/plexNAS/Files/tv/" # Directory where files will be generated (make sure there is a "/" at the end!)
timezone = "-0400" # Enter Timezone
showPoster = "http://toddamurphy.me/logos/todderang.png"
channelName = "Todderang"

########################################################
########################################################
#                       END                            #
########################################################
########################################################


cartoons1 = ["1973 Super Friends", "1977 The All-New Super Friends Hour", "1978 Challenge of the SuperFriends", "1979 The World's Greatest Super Friends",
             "1984 Super Friends The Legendary Super Powers Show", "1985 The Super Powers Team Galactic Guardians", "A Pup Named Scooby Doo", "Baby Looney Tunes", "Courage The Cowardly Dog",
             "Dexter's Laboratory", "Ed,Edd n' Eddy", "Hong Kong Phooey", "Josie and the Pussycats", "Popeye", "Scooby Doo, Where Are You", "Snagglepuss", "Speed Buggy",
             "SuperFriends(1980)", "The 13 Ghosts Of Scooby-Doo", "The Flintstones", "The Jetsons", "The Looney Tunes Show", "The New Scooby-Doo Movies",
             "The Pink Panther Cartoon", "The Smurfs", "The Super Friends", "Yogi Bear Show", "Tom & Jerry"]
cartoonsLeft = cartoons.copy()
showDirectory = []
previousRandomShow = 999
playlistDuration = 0
showDurations = []
showName = ""
showDesc = ""
showCounter = 0
showLength = 0
blockCounter = 0


extensions = ['.264', '.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.3mm', '.3p2', '.60d', '.787', '.89', '.aaf', '.aec', '.aep', '.aepx',
              '.aet', '.aetx', '.ajp', '.ale', '.am', '.amc', '.amv', '.amx', '.anim', '.aqt', '.arcut', '.arf', '.asf', '.asx', '.avb',
              '.avc', '.avd', '.avi', '.avp', '.avs', '.avs', '.avv', '.axm', '.bdm', '.bdmv', '.bdt2', '.bdt3', '.bik', '.bin', '.bix',
              '.bmk', '.bnp', '.box', '.bs4', '.bsf', '.bvr', '.byu', '.camproj', '.camrec', '.camv', '.ced', '.cel', '.cine', '.cip',
              '.clpi', '.cmmp', '.cmmtpl', '.cmproj', '.cmrec', '.cpi', '.cst', '.cvc', '.cx3', '.d2v', '.d3v', '.dat', '.dav', '.dce',
              '.dck', '.dcr', '.dcr', '.ddat', '.dif', '.dir', '.divx', '.dlx', '.dmb', '.dmsd', '.dmsd3d', '.dmsm', '.dmsm3d', '.dmss',
              '.dmx', '.dnc', '.dpa', '.dpg', '.dream', '.dsy', '.dv', '.dv-avi', '.dv4', '.dvdmedia', '.dvr', '.dvr-ms', '.dvx', '.dxr',
              '.dzm', '.dzp', '.dzt', '.edl', '.evo', '.eye', '.ezt', '.f4p', '.f4v', '.fbr', '.fbr', '.fbz', '.fcp', '.fcproject', '.ffd',
              '.flc', '.flh', '.fli', '.flv', '.flx', '.gfp', '.gl', '.gom', '.grasp', '.gts', '.gvi', '.gvp', '.h264', '.hdmov', '.hkm',
              '.ifo', '.imovieproj', '.imovieproject', '.ircp', '.irf', '.ism', '.ismc', '.ismv', '.iva', '.ivf', '.ivr', '.ivs', '.izz',
              '.izzy', '.jss', '.jts', '.jtv', '.k3g', '.kmv', '.ktn', '.lrec', '.lsf', '.lsx', '.m15', '.m1pg', '.m1v', '.m21', '.m21',
              '.m2a', '.m2p', '.m2t', '.m2ts', '.m2v', '.m4e', '.m4u', '.m4v', '.m75', '.mani', '.meta', '.mgv', '.mj2', '.mjp', '.mjpg',
              '.mk3d', '.mkv', '.mmv', '.mnv', '.mob', '.mod', '.modd', '.moff', '.moi', '.moov', '.mov', '.movie', '.mp21', '.mp21',
              '.mp2v', '.mp4', '.mp4v', '.mpe', '.mpeg', '.mpeg1', '.mpeg4', '.mpf', '.mpg', '.mpg2', '.mpgindex', '.mpl', '.mpl',
              '.mpls', '.mpsub', '.mpv', '.mpv2', '.mqv', '.msdvd', '.mse', '.msh', '.mswmm', '.mts', '.mtv', '.mvb', '.mvc', '.mvd',
              '.mve', '.mvex', '.mvp', '.mvp', '.mvy', '.mxf', '.mxv', '.mys', '.ncor', '.nsv', '.nut', '.nuv', '.nvc', '.ogm', '.ogv', '.ogx',
              '.osp', '.otrkey', '.pac', '.par', '.pds', '.pgi', '.photoshow', '.piv', '.pjs', '.playlist', '.plproj', '.pmf', '.pmv', '.pns',
              '.ppj', '.prel', '.pro', '.prproj', '.prtl', '.psb', '.psh', '.pssd', '.pva', '.pvr', '.pxv', '.qt', '.qtch', '.qtindex', '.qtl',
              '.qtm', '.qtz', '.r3d', '.rcd', '.rcproject', '.rdb', '.rec', '.rm', '.rmd', '.rmd', '.rmp', '.rms', '.rmv', '.rmvb', '.roq', '.rp',
              '.rsx', '.rts', '.rts', '.rum', '.rv', '.rvid', '.rvl', '.sbk', '.sbt', '.scc', '.scm', '.scm', '.scn', '.screenflow', '.sec',
              '.sedprj', '.seq', '.sfd', '.sfvidcap', '.siv', '.smi', '.smi', '.smil', '.smk', '.sml', '.smv', '.spl', '.sqz', '.srt', '.ssf',
              '.ssm', '.stl', '.str', '.stx', '.svi', '.swf', '.swi', '.swt', '.tda3mt', '.tdx', '.thp', '.tivo', '.tix', '.tod', '.tp', '.tp0',
              '.tpd', '.tpr', '.trp', '.ts', '.tsp', '.ttxt', '.tvs', '.usf', '.usm', '.vc1', '.vcpf', '.vcr', '.vcv', '.vdo', '.vdr', '.vdx',
              '.veg', '.vem', '.vep', '.vf', '.vft', '.vfw', '.vfz', '.vgz', '.vid', '.video', '.viewlet', '.viv', '.vivo', '.vlab', '.vob',
              '.vp3', '.vp6', '.vp7', '.vpj', '.vro', '.vs4', '.vse', '.vsp', '.w32', '.wcp', '.webm', '.wlmp', '.wm', '.wmd', '.wmmp', '.wmv',
              '.wmx', '.wot', '.wp3', '.wpl', '.wtv', '.wve', '.wvx', '.xej', '.xel', '.xesc', '.xfl', '.xlmv', '.xmv', '.xvid', '.y4m', '.yog',
              '.yuv', '.zeg', '.zm1', '.zm2', '.zm3', '.zmv']


print("#####GENERATING SHOW LIST#####")


########################################################
# Writes to the show list
########################################################
def writeToArray(path):
    global tempShowList
    global extensions

    ext = os.path.splitext(path)[-1].lower()

    if ext in extensions:
        tempShowList.append(path)
        #print("Added: " + path)
########################################################
        

########################################################
# Check duration of file
########################################################
def checkDuration(file):
    try:
        return mp.VideoFileClip(file).duration
    except OSError:
        print("Could not get duration for: " + file)
        return 1799  # default value if it fails
########################################################


########################################################
# Generate episdoe list that fit into 40min -1hr block
########################################################
def generateBlock(episodes):
    global playlistDuration
    returnList = []
    durationCheck = False
    totalDuration = 0

    while not durationCheck:
        randomChoice = random.choice(episodes)
        currentDuration = checkDuration(randomChoice)
        totalDuration += currentDuration
        playlistDuration += currentDuration

        if totalDuration < 3600:
            returnList.append(randomChoice)
        else:
            durationCheck = True
    return returnList
########################################################

    
# Loops into individual directories to get directly to files
while len(cartoonsLeft) != 0:
    tempShowList = []
    randomNumber = random.randint(0, len(cartoonsLeft)-1)
    currentShow = cartoonsLeft[randomNumber]
    cartoonsLeft.remove(currentShow)

    for file in os.listdir(dir + currentShow):
        if "Specials" in file or "Subs" in file: #omit specials, extras, subtitles and deleted scenes
            continue
        if os.path.isfile(dir + currentShow + "/" + file):
            writeToArray(dir + currentShow + "/" + file)
        else:
            for seasonFile in os.listdir(dir + currentShow + "/" + file):
                writeToArray(dir + currentShow + "/" + file + "/" + seasonFile)
    showDirectory.append(tempShowList.copy())
    
# Open Files
if not backup:
    tvList = open(tvDirectory + "showList.txt", "w")
    m3u = open(tvDirectory + "playlist.m3u", "w")
else:
    tvList = open(tvDirectory + "showList1.txt", "w")
    m3u = open(tvDirectory + "playlist1.m3u", "w")
xmltv = open(tvDirectory + "temp_xmltv.xml", "w")

# Initial line in M3U file
m3u.write("#EXTM3U\n")

# Initial line for xmltv
xmltv.write("<tv generator-info-name='Todd' source-info-name='Todds Generator'>\n")
xmltv.write("<channel id='1'>\n")
xmltv.write("<display-name>" + channelName + "</display-name>\n")
xmltv.write("<icon src='" + showPoster + "'/>\n")
xmltv.write("</channel>\n")

# Generate Blocks of Episodes & puts back into directory
while blockCounter < len(showDirectory):
    print ("Generating Blocks..." + str(len(showDirectory) - blockCounter) + " left.")
    showDirectory[blockCounter] = generateBlock(showDirectory[blockCounter])
    blockCounter += 1

# Loops through show directory and generate random schedule
while len(showDirectory) > 0:
    randomShow = random.randint(0, len(showDirectory)-1) # already a random show because populated in random order
    #print ("Random Number: " + str(randomShow))

    while len(showDirectory[randomShow]) > 0:
        randomEpisode = random.choice(showDirectory[randomShow])
        randomEpisodeWrite = randomEpisode.encode('utf-8').strip().decode()

        # Get Name of Show
        showName = randomEpisode.split(dir)[1].split('/')[0]
        
        # Get Description of Show (Episode Name)
        showDesc = os.path.basename(randomEpisode)
        showDesc = os.path.splitext(showDesc)[0]

        print("Writing: " + randomEpisode)
        
        # Write episode to txt file
        tvList.write(randomEpisodeWrite)
        tvList.write("\n")

        #Need to get duration for XML and array
        cur_duration = checkDuration(randomEpisode)

        # Write episode to m3u file
        m3u.write("#EXTINF: " + str(cur_duration) + "," + showDesc + "\n")
        m3u.write("file://" + randomEpisodeWrite + "\n")

        # Write episode to xmltv file
        xmltv.write("<programme channel='1' start='{tempStartTime} " + timezone + "' stop='{tempEndTime} " + timezone + "'>\n")
        xmltv.write("<title lang='en'>" + showName + "</title>\n")
        xmltv.write("<desc lang='en'>" + showDesc + "</desc>\n")
        xmltv.write("<icon height='' src='" + showPoster + "' width=''/>\n")
        xmltv.write("<video/>\n<date/>\n<new/>\n</programme>\n")

        # Add Episode and Duration to dictionary
        showDurations.append(math.ceil(cur_duration))

        # Remove the episode
        #print ("Removing: " + randomEpisode)
        showDirectory[randomShow].remove(randomEpisode)

    # Remove show
    del showDirectory[randomShow]

# Close xmltv
xmltv.write("</tv>")

# Close files
tvList.close()
m3u.close()
xmltv.close()

# Replace time in xmltv files
## Need to do this after execution b/c script takes long to execute
f1 = open(tvDirectory + 'temp_xmltv.xml', 'r')
if not backup:
    f2 = open(tvDirectory + 'xmltv.xml', 'w')
else:
    f2 = open(tvDirectory + 'xmltv1.xml', 'w')

timeObject = datetime.now()

for line in f1:
    # Replace & with correct escape
    line = line.replace('&', '&amp;')
    
    if '{tempStartTime}' in line:
        showLength = showDurations[showCounter]
        currentTime = timeObject.strftime("%Y%m%d%H%M%S")
        line = line.replace('{tempStartTime}', str(currentTime))
        timeObject += timedelta(seconds=showLength)
        currentTime = timeObject.strftime("%Y%m%d%H%M%S")
        line = line.replace('{tempEndTime}', str(currentTime))

        # Increase show counter
        showCounter += 1
        
    f2.write(line)
    
# Close xmltv
f1.close()
f2.close()

print ("Playlist Duration in seconds: " + str(playlistDuration))
print("Finished! Happy Streaming!")
