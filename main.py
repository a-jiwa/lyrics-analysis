from bs4 import BeautifulSoup

html = """<ul>
				<li class="page_item page-item-1004"><a href="https://uk-drill.com/12-om/">12/OM</a></li>
<li class="page_item page-item-1023"><a href="https://uk-drill.com/12world-12anti/">12World/12Anti</a></li>
<li class="page_item page-item-1016"><a href="https://uk-drill.com/156-2/">156</a></li>
<li class="page_item page-item-814"><a href="https://uk-drill.com/7th-gang-profile/">7th WoodGrange x BWC Gang Profile</a></li>
<li class="page_item page-item-1007"><a href="https://uk-drill.com/9iners/">9iners</a></li>
<li class="page_item page-item-1053"><a href="https://uk-drill.com/9th-street/">9th Street</a></li>
<li class="page_item page-item-993"><a href="https://uk-drill.com/acg-6th/">ACG/6th</a></li>
<li class="page_item page-item-1033"><a href="https://uk-drill.com/active-gang/">Active Gang</a></li>
<li class="page_item page-item-1513"><a href="https://uk-drill.com/archive/">Archive</a></li>
<li class="page_item page-item-973"><a href="https://uk-drill.com/ay-aylesbury-estate/">AY/Aylesbury Estate</a></li>
<li class="page_item page-item-980"><a href="https://uk-drill.com/b-side/">B-Side</a></li>
<li class="page_item page-item-983"><a href="https://uk-drill.com/block-6/">Block 6</a></li>
<li class="page_item page-item-977"><a href="https://uk-drill.com/browning17/">Browning17</a></li>
<li class="page_item page-item-1001"><a href="https://uk-drill.com/cge/">CGE</a></li>
<li class="page_item page-item-1024"><a href="https://uk-drill.com/church-road/">Church Road</a></li>
<li class="page_item page-item-254"><a href="https://uk-drill.com/contact-us/">Contact us / Disclaimer</a></li>
<li class="page_item page-item-1036"><a href="https://uk-drill.com/cumbo/">Cumbo</a></li>
<li class="page_item page-item-998"><a href="https://uk-drill.com/custom-house/">Custom House</a></li>
<li class="page_item page-item-867"><a href="https://uk-drill.com/deep/">Deep</a></li>
<li class="page_item page-item-1546"><a href="https://uk-drill.com/eas-reuploads/">Eas Reuploads</a></li>
<li class="page_item page-item-851"><a href="https://uk-drill.com/east/">East</a></li>
<li class="page_item page-item-243"><a href="https://uk-drill.com/uk-drill-editorial-articles-blog/">Editorials</a></li>
<li class="page_item page-item-261 page_item_has_children"><a href="https://uk-drill.com/gangs/">Gangs</a>
<ul class="children">
	<li class="page_item page-item-528"><a href="https://uk-drill.com/gangs/cb-7th/">CB (Crazy Blackz, Blackz) 7th</a></li>
	<li class="page_item page-item-547"><a href="https://uk-drill.com/gangs/digga-d/">Digga D</a></li>
	<li class="page_item page-item-779"><a href="https://uk-drill.com/gangs/east/">East</a></li>
	<li class="page_item page-item-543"><a href="https://uk-drill.com/gangs/trizzac/">LD/SCRIBZ 67</a></li>
	<li class="page_item page-item-521"><a href="https://uk-drill.com/gangs/yanko/">Mizormac Harlem Spartans</a></li>
	<li class="page_item page-item-777 page_item_has_children"><a href="https://uk-drill.com/gangs/north/">North</a>
	<ul class="children">
		<li class="page_item page-item-757"><a href="https://uk-drill.com/gangs/north/3x3/">3×3 Gang</a></li>
	</ul>
</li>
	<li class="page_item page-item-530"><a href="https://uk-drill.com/gangs/hitman-x-da/">PS ZONE II</a></li>
	<li class="page_item page-item-534"><a href="https://uk-drill.com/gangs/burner/">SJ OFB</a></li>
	<li class="page_item page-item-781"><a href="https://uk-drill.com/gangs/south/">South</a></li>
	<li class="page_item page-item-783"><a href="https://uk-drill.com/gangs/west/">West</a></li>
</ul>
</li>
<li class="page_item page-item-1372"><a href="https://uk-drill.com/gb-rhyheim-barton/">GB – Rhyheim Barton</a></li>
<li class="page_item page-item-831"><a href="https://uk-drill.com/glossary/">Glossary</a></li>
<li class="page_item page-item-970"><a href="https://uk-drill.com/harlem-spartans/">Harlem Spartans</a></li>
<li class="page_item page-item-846"><a href="https://uk-drill.com/history-of-gangs/">History of Gangs</a></li>
<li class="page_item page-item-242"><a href="https://uk-drill.com/">Home</a></li>
<li class="page_item page-item-1028"><a href="https://uk-drill.com/hrb/">HRB</a></li>
<li class="page_item page-item-967"><a href="https://uk-drill.com/kuku/">Kuku</a></li>
<li class="page_item page-item-1373"><a href="https://uk-drill.com/lil-zac/">Lil Zac</a></li>
<li class="page_item page-item-1013"><a href="https://uk-drill.com/mali-strip/">Mali Strip</a></li>
<li class="page_item page-item-962"><a href="https://uk-drill.com/moscow-17/">Moscow 17</a></li>
<li class="page_item page-item-936"><a href="https://uk-drill.com/n15/">N15</a></li>
<li class="page_item page-item-1376"><a href="https://uk-drill.com/negus/">Negus</a></li>
<li class="page_item page-item-1375"><a href="https://uk-drill.com/nesha/">Nesha</a></li>
<li class="page_item page-item-355"><a href="https://uk-drill.com/new-music/">New Music</a></li>
<li class="page_item page-item-850"><a href="https://uk-drill.com/north/">North</a></li>
<li class="page_item page-item-1900"><a href="https://uk-drill.com/north-2/">north</a></li>
<li class="page_item page-item-1543"><a href="https://uk-drill.com/north-reuploads/">North Reuploads</a></li>
<li class="page_item page-item-1038"><a href="https://uk-drill.com/nw/">North West</a></li>
<li class="page_item page-item-1545"><a href="https://uk-drill.com/north-west-reuploads/">North West Reuploads</a></li>
<li class="page_item page-item-952"><a href="https://uk-drill.com/npk-northumberland-park-kids/">NPK/Northumberland Park Kids</a></li>
<li class="page_item page-item-947"><a href="https://uk-drill.com/omh-manor-house/">OMH/Manor House</a></li>
<li class="page_item page-item-1025"><a href="https://uk-drill.com/original-3rd/">Original 3rd</a></li>
<li class="page_item page-item-1044"><a href="https://uk-drill.com/peckwater/">Peckwater</a></li>
<li class="page_item page-item-1374"><a href="https://uk-drill.com/perry/">Perry</a></li>
<li class="page_item page-item-1015"><a href="https://uk-drill.com/rayners-lane/">Rayners Lane</a></li>
<li class="page_item page-item-826"><a href="https://uk-drill.com/rude-drill-songs/">Rude Drill Songs</a></li>
<li class="page_item page-item-986"><a href="https://uk-drill.com/siraq/">Siraq</a></li>
<li class="page_item page-item-927"><a href="https://uk-drill.com/skengfield-ap/">Skengfield/AP</a></li>
<li class="page_item page-item-1377"><a href="https://uk-drill.com/skengz/">Skengz</a></li>
<li class="page_item page-item-852"><a href="https://uk-drill.com/sout/">Sout</a></li>
<li class="page_item page-item-1544"><a href="https://uk-drill.com/south-reuploads/">South Reuploads</a></li>
<li class="page_item page-item-939"><a href="https://uk-drill.com/tpl/">TPL Gang</a></li>
<li class="page_item page-item-1370"><a href="https://uk-drill.com/tributes/">Tributes</a></li>
<li class="page_item page-item-274 page_item_has_children"><a href="https://uk-drill.com/beats/">UK Drill Beats</a>
<ul class="children">
	<li class="page_item page-item-690"><a href="https://uk-drill.com/beats/uk-drill-drum-kits/">UK Drill Drum Kits</a></li>
</ul>
</li>
<li class="page_item page-item-838"><a href="https://uk-drill.com/drill-map/">UK Drill Gang Map</a></li>
<li class="page_item page-item-899"><a href="https://uk-drill.com/slang-cheatsheet/">UK Drill Slang “cheatsheet”</a></li>
<li class="page_item page-item-942"><a href="https://uk-drill.com/v8-hornsey/">V8/Hornsey</a></li>
<li class="page_item page-item-854"><a href="https://uk-drill.com/west/">West</a></li>
<li class="page_item page-item-1547"><a href="https://uk-drill.com/west-reuploads/">West Reuploads</a></li>
<li class="page_item page-item-844 page_item_has_children"><a href="https://uk-drill.com/wgm-woodgreenmob/">WGM (WoodGreenMOB)</a>
<ul class="children">
	<li class="page_item page-item-1735"><a href="https://uk-drill.com/wgm-woodgreenmob/l/">.l</a></li>
</ul>
</li>
<li class="page_item page-item-1010"><a href="https://uk-drill.com/zero-tolerance/">Zero Tolerance</a></li>
			</ul>"""

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Create a list to store the data
data_list = []

# Find all the <li> elements
list_items = soup.find_all('li', class_='page_item')

# Loop through the <li> elements and extract the data
for item in list_items:
    item_data = {}

    # Extract the text inside the <a> tag
    item_data['text'] = item.a.get_text()

    # Extract the 'href' attribute
    item_data['link'] = item.a['href']

    data_list.append(item_data)

# Print the cleaned data
for item in data_list:
    print(item)