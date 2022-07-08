import spacy
from spacy.matcher import Matcher
import syllapy
import random
import snscrape.modules.twitter as sntwitter
import pandas as pd
import html
import re
import pyfiglet
import cowsay
from colorama import init, Fore, Back, Style
init(autoreset = True)


#Twitter Stuff
#query = "(#cyber) until:2022-07-30 since:2022-01-01"
print('\n')
print(Fore.CYAN + Style.BRIGHT +"█▓▒▒░░░░░░░░░░░░░░░░░░░░░░░=ƬЩIƬƬΣЯ ΉΛIKЦ MΛKΣЯ=░░░░░░░░░░░░░░░░░░░░░░░▒▒▓█")
print(Fore.BLUE + Style.DIM +'''
                                             23
                                           23232
                                   232\/2 323
                                        23|,/  |/2 32
    _______________________              23/   /  /_2  32
   / I query Twitter         \             \  {  |_____/_2
   | To bring you chaos poem  |            {  / /          232
   \ Thanks for all the hacks /            `, \{___________/_23
     ------------------------               } }{       \\
             \   ^__^                       }||         \____2
              \  (0o)\_______              ||{           `3_23
                 (__)\       )\/\          ||}             23
                     ||----23|       , -=-~{ .-^- _
                     ||     ||             `}
                                            {''')
print(Fore.BLUE + Style.NORMAL + '''
+---------------+---------------------------------------------------------+
| Query Syntax: |  (#cyber) until:2022-07-30 since:2022-01-01             |
+---------------+---------------------------------------------------------+
| Examples      | (@corykennedy "nano") until:2022-07-30 since:2010-01-01 |
|               | (from:securiteestar) until:2022-07-30 since:2022-01-01  |
|               | (#hacking) until:2022-07-30 since:2010-01-01            |
|               | (from:sec_kc to:corykennedy)                            |
+---------------+---------------------------------------------------------+''')
query = input(Fore.CYAN + Style.BRIGHT + "𝙴𝚗𝚝𝚎𝚛 𝚃𝚠𝚒𝚝𝚝𝚎𝚛 𝚀𝚞𝚎𝚛𝚢 >> " + Fore.MAGENTA + Style.BRIGHT)
print('\n')  
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.content])
        #tweets.append([tweet.username, tweet.content])
pd.set_option('display.max_colwidth', 100)        
tweet_df = pd.DataFrame(tweets, columns=['Tweet'])
logfile = query + '.log'
logfile = re.sub('[()$@&:#" __]','',logfile)
#print(logfile)

for tweet in tweets:
    cleaned = html.unescape(tweet[0].strip())
    tweetlog = open(logfile, 'a')
    tweetlog.write("%s\n" % cleaned)
    tweetlog.close()


#pip3 install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.0.0/en_core_web_sm-3.0.0.tar.gz 
nlp = spacy.load("en_core_web_sm")
matcher2 = Matcher(nlp.vocab)
matcher3 = Matcher(nlp.vocab)
matcher4 = Matcher(nlp.vocab)
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'POS':  {"IN": ["NOUN", "VERB"]} }]
matcher2.add("TwoWords", [pattern])
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher3.add("ThreeWords", [pattern])
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher4.add("FourWords", [pattern])
doc = nlp(open(logfile).read())
matches2 = matcher2(doc)
matches3 = matcher3(doc)
matches4 = matcher4(doc)
g_5 = []
g_7 = []
for match_id, start, end in matches2 + matches3 + matches4:
    string_id = nlp.vocab.strings[match_id]  # Get string representation
    span = doc[start:end]  # The matched span
    syl_count = 0
    for token in span:
        syl_count += syllapy.count(token.text)
    if syl_count == 5:
        if span.text not in g_5:
            g_5.append(span.text)
    if syl_count == 7:
        if span.text not in g_7:
            g_7.append(span.text)
print(Fore.BLUE + Style.BRIGHT + " 卩尺乇丂丂 乇几ㄒ乇尺 ㄒㄖ ㄚ乇乇ㄒ ㄖㄩㄒ 卂几ㄖㄒ卄乇尺 卄卂Ҝ匚乇尺-卄卂丨Ҝㄩ  \n")
print(Fore.BLUE + Style.BRIGHT + "                             ^𝖢 𝗍𝗈 𝗊𝗎𝗂𝗍                                 \n")
while (True):
    hakciu = ("%s\n%s\n%s" %(random.choice(g_5),random.choice(g_7),random.choice(g_5)))
    #hakcermode = cowsay.cow(hakciu)
    print(Fore.MAGENTA + Style.BRIGHT +'\n')
    print(cowsay.get_output_string('ghostbusters', Fore.MAGENTA + Style.BRIGHT + hakciu))
    print('\n')
    print(Fore.BLUE + Style.BRIGHT + "卩尺乇丂丂 乇几ㄒ乇尺 ㄒㄖ ㄚ乇乇ㄒ ㄖㄩㄒ 卂几ㄖㄒ卄乇尺 卄卂Ҝ匚乇尺-卄卂丨Ҝㄩ\n")
    print(Fore.BLUE + Style.BRIGHT + "                                ^𝖢 𝗍𝗈 𝗊𝗎𝗂𝗍                                 \n")
    print(Fore.MAGENTA + Style.BRIGHT +'\n')
    input("\n")
    