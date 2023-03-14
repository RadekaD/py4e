# Find the host of your professors email and go to the webpage

import webbrowser

data = "from:	Bojan Vranic <bojan.vranic@fpn.bg.ac.rs> Feb 24, 2021, 2:45 PM"
atpos = data.find("@")

sppos = data.find(" ", atpos)

host = data[atpos+1 : sppos-1]

webbrowser.open(f"http://{host}")