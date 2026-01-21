import requests
import sys
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

OPPGAVE_URL = "https://leetcode.com/problems/{oppgave}"


def request_oppgaveinfo():
    url = "https://leetcode.com/graphql"
    query = "query { allQuestions { title titleSlug difficulty topicTags { name slug } }}"

    response = requests.post(url, json={"query": query})
    return {e['title']: (e['difficulty'], [el['name'] for el in e['topicTags']], e['titleSlug']) for e in response.json()["data"]["allQuestions"]}

oppgaveinfo = request_oppgaveinfo()
løste = {e.stem: e for p in Path("løsninger").iterdir() for e in list(p.iterdir())}

tagkategorisert = defaultdict(set)
for løst in løste:
    nr,oppgave = løst.split("-", 1)
    for tag in oppgaveinfo[oppgave][1]:
        tagkategorisert[tag].add(løst)

def færrest_tags_som_dekker_alle_oppgaver(tagkategorisert):
    # Set Cover Problem: Problemet er NP-hard
    #     
    udekkede = set(e for p in tagkategorisert.values() for e in p)
    valgte_tagger = set()

    while udekkede:
        best_tag = max(tagkategorisert, key=lambda t: len(tagkategorisert[t] & udekkede))
        dekket = tagkategorisert[best_tag] & udekkede

        if not dekket:
            break  # no progress possible

        udekkede -= dekket
        valgte_tagger.add(best_tag)
    return valgte_tagger

tagger = færrest_tags_som_dekker_alle_oppgaver(tagkategorisert)

brukte = set()
oppgaver_fordelt = defaultdict(list)
for tag in sorted(tagger, key=lambda x: len(tagkategorisert[x])):
    for oppgave in tagkategorisert[tag]:
        if oppgave in brukte:
            continue
        brukte.add(oppgave)
        oppgaver_fordelt[tag].append(oppgave)
    oppgaver_fordelt[tag] = list(sorted(oppgaver_fordelt[tag], key=lambda x: int(x.split("-",1)[0])))

for tag in sorted(tagger, key=lambda x: len(oppgaver_fordelt[x]), reverse=True):
    print(tag)
    print("-----")
    for el in oppgaver_fordelt[tag]:
        print(el)
    print("")


with open("README.md", "w", encoding="utf-8") as f:
    f.write("# LeetCode\n\n")

    f.write(f"Totalt **{len(brukte)}** oppgaver løst.\n\n")    
    f.write("<ul>\n")    
    for tag in sorted(tagger, key=lambda x: len(oppgaver_fordelt[x]), reverse=True):
        f.write(f"\t<details>\n\t<summary>\n")
        f.write(f"\t\t\t<strong>{tag} ({len(oppgaver_fordelt[tag])})</strong><br>\n\t\t\t")
        for oppgave in oppgaver_fordelt[tag]:
            nr,tittel = oppgave.split("-", 1)
            vanskelighetsgrad = oppgaveinfo[tittel][0]

            status = "🟩" if vanskelighetsgrad == "Easy" else ("🟨" if vanskelighetsgrad == "Medium" else "🟥")
            
            f.write(status)
        
        f.write("\n\t\t</summary>")
    
        f.write("\n\t\t<table>")
        for oppgave in oppgaver_fordelt[tag]:
            f.write("\n\t\t\t<tr>")
            
            nr,tittel = oppgave.split("-", 1)
            vanskelighetsgrad = oppgaveinfo[tittel][0]

            f.write(f"\n\t\t\t\t<td>{nr}</td>")
            f.write(f'''\n\t\t\t\t<td>\n\t\t\t\t\t<a href="{OPPGAVE_URL.replace('{oppgave}', oppgaveinfo[tittel][2])}">{tittel}</td>''')
            f.write(f'\n\t\t\t\t<td>{vanskelighetsgrad}</td>')
            f.write(f'''\n\t\t\t\t<td><a href="{løste[oppgave]}">🔍</a></td>''')
            f.write("\n\t\t\t</tr>")
        
        f.write("\n\t\t</table>")

        f.write("\n\t</details>")
        f.write("\n\t<br>\n")
    f.write("</ul>\n")
        

#for løst in løste:
#    nr,oppgave = løst.split("-", 1)
#    print(oppgaveinfo[oppgave])





#print(konkurransemapper)

#for el in konkurransemapper:
    
