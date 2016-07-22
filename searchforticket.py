import threading
import urllib2
import os
import ctypes

t = None

def searchforticket():
    global t
    url = "https://in.bookmyshow.com/buytickets/kabali-chennai/movie-chen-ET00039091-MT/20160722"
    #url = "http://www.quora.com"
    #run_cmd = 'start C:/Users/naveenkumar/Music/Thani_Oruvan/Aasai_Perasai-MassTamilan.com.mp3'
    run_cmd = 'start '+url;
    search_str = 'mayajaal,<div data-online="Y">'
    search_str = search_str.lower()
    search_strings = search_str.split(",")

    req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    t = threading.Timer(10.0, searchforticket)
    t.start();
    print "Searching...",url
    data = urllib2.urlopen(req).read()
    data = data.lower();
	
    i = 1;
    found = False;
    for search_string in search_strings:
        found = False;
        if( search_string in data):
            #ctypes.windll.user32.MessageBoxA(0, "Found search string: "+search_string, "String found "+(str(i)), 1)
            i = i + 1
            found = True;
            #os.system(run_cmd)
            #if(t.is_alive()):
                #t.cancel();            

    if(found == True):
        ctypes.windll.user32.MessageBoxA(0, "Found search string: "+'-'.join(search_strings), "STRING FOUND", 1)
        os.system(run_cmd)
        if(t.is_alive()):
            t.cancel();
            
searchforticket();
