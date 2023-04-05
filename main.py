from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
from random import randint

l = ["DOPAMINE DETOX ", "MINMAL BASE MOTION ", "ESCAPISM ", "PROGRESSIVE OVERLOAD ", "MINIMAL BASE STIMULATION ", "TIMINGS ", "DIVIDE AND CONQUER ", "MIND OVER BODY ", "TOP-DOWN CONTROL "]
l = list(map(lambda x:x*randint(0,len(l)),l))
txt = ''.join(s for s in l)
#wc = WordCloud().generate(txt)
#plt.imshow(wc)
#plt.axis("off")
#plt.show()

f = {"DOPAMINE DETOX ":randint(0,10),"MINMAL BASE MOTION ":randint(0,10), "ESCAPISM ":randint(0,10), "PROGRESSIVE OVERLOAD ":randint(0,10), "MINIMAL BASE STIMULATION ":randint(0,10), "TIMINGS ":randint(0,10), "DIVIDE AND CONQUER ":randint(0,10), "MIND OVER BODY ":randint(0,10), "TOP-DOWN CONTROL ":randint(0,10), "GROWTH MENTALITY":randint(0,10)}
wc2 = WordCloud().generate_from_frequencies(f)
plt.imshow(wc2)
plt.axis("off")
plt.show()
