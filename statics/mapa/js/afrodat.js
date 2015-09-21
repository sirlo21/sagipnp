/** 
 * afrodat.js 1.0 (20-Apr-2011)
 * (c) by Christian Effenberger 
 * All Rights Reserved
 * Source: mapzoom.netzgesta.de

afrodat format: (utf-8)
	index ISO-3166 2-letter code
	lc == ISO-3166 3-letter code
	nc == ISO-3166 numerical code
	sn == ISO-3166 int. eng. country/state/local area name
	cc == ISO-3166 int. eng. continent/global area name
	cn == ISO-3166 int. eng. country/state capital name
	lm == typical landmark of the country
	bw == bounding border coordinate west [-180|+180 float]
	be == bounding border coordinate east [-180|+180 float]
	bn == bounding border coordinate north [-90|+90 float]
	bs == bounding border coordinate south [-90|+90 float]
	// coordbox:[37.5,-20,-34.5,52]
**/

var afrodat = new Array();
afrodat["africa"] = {
	DZ: {nc:'012',lc:'DZA',cn:'Algers',cc:'Africa',sn:'Algeria',lm:'Makam Echahid',bw:-8.67386913299561,bn:37.0937271118164,be:11.979549407959,bs:18.9600257873535},
	AO: {nc:'024',lc:'AGO',cn:'Luanda',cc:'Africa',sn:'Angola',lm:'Tazua Falls',bw:11.679217338562,bn:-4.3768253326416,be:24.0821228027344,bs:-18.0420780181885},
	BJ: {nc:'204',lc:'BEN',cn:'Port-Novo',cc:'Africa',sn:'Benin',lm:'Royal Palaces of Abomey',bw:0.774574935436249,bn:12.4183483123779,be:3.85170125961304,bs:6.22574710845947},
	BW: {nc:'072',lc:'BWA',cn:'Gaborone',cc:'Africa',sn:'Botswana',lm:'Okavango Delta',bw:19.999532699585,bn:-17.7808094024658,be:29.3607845306396,bs:-26.9072494506836},
	BF: {nc:'854',lc:'BFA',cn:'Ouagadougou',cc:'Africa',sn:'Burkina Faso',lm:'Acacia Savanna',bw:-5.51891660690308,bn:15.082594871521,be:2.40539526939392,bs:9.40110683441162},
	//BI: position
	CM: {nc:'120',lc:'CMR',cn:'Yaounde',cc:'Africa',sn:'Cameroon',lm:'Bamoum Sultan Palace',bw:8.49476146697998,bn:13.0780572891235,be:16.1921195983887,bs:1.65254783630371},
	CF: {nc:'140',lc:'CAF',cn:'Bangui',cc:'Africa',sn:'Central African Republic',lm:'Dzangha-Sangha National Park',bw:14.4200954437256,bn:11.0075702667236,be:27.4634246826172,bs:2.22051358222961},
	TD: {nc:'148',lc:'TCD',cn:"N'Djamena",cc:'Africa',sn:'Chad',lm:'Ennedi Range',bw:13.4734735488892,bn:23.4503726959229,be:24.00266456604,bs:7.44106721878052},
	CG: {nc:'178',lc:'COG',cn:'Brazzaville',cc:'Africa',sn:'Republic of the Congo',lm:'Livingstone Falls',bw:11.2050075531006,bn:3.70308232307434,be:18.6498413085938,bs:-5.02722358703613},
	CD: {nc:'180',lc:'COD',cn:'Kinshasa',cc:'Africa',sn:'Democratic Republic of the Congo',lm:'Okapi Wildlife Reserve',bw:12.2041425704956,bn:5.38609886169434,be:31.3059139251709,bs:-13.4556760787964},
	DJ: {nc:'262',lc:'DJI',cn:'Djibouti',cc:'Africa',sn:'Djibouti',lm:'Lac Assal',bw:41.7734680175781,bn:12.7068347930908,be:43.4169769287109,bs:10.9099159240723},
	EG: {nc:'818',lc:'EGY',cn:'Cairo',cc:'Africa',sn:'Egypt',lm:'Giza Pyramids',bw:24.6981086730957,bn:31.6673374176025,be:35.7948684692383,bs:21.7253856658936},
	GQ: {nc:'226',lc:'GNQ',cn:'Malabo',cc:'Africa',sn:'Equatorial Guinea',lm:'Pico Basile',bw:9.34686374664307,bn:2.34698939323425,be:11.3357257843018,bs:0.920859932899475},
	ER: {nc:'232',lc:'ERI',cn:'Asmara',cc:'Africa',sn:'Eritrea',lm:'Nda Mariam Othodox Church',bw:36.4387741088867,bn:18.0030860900879,be:43.1346473693848,bs:12.3595533370972},
	ET: {nc:'231',lc:'ETH',cn:'Addis Ababa',cc:'Africa',sn:'Ethiopia',lm:'King Fasilides Castle',bw:32.9999351501465,bn:14.8937511444092,be:47.9861831665039,bs:3.40242171287537},
	GA: {nc:'266',lc:'GAB',cn:'Liberville',cc:'Africa',sn:'Gabon',lm:'Lope-Okanda',bw:8.69546985626221,bn:2.32261228561401,be:14.5023488998413,bs:-3.97880625724792},
	//GM: position
	GH: {nc:'288',lc:'GHA',cn:'Accra',cc:'Africa',sn:'Ghana',lm:'Independence Arch',bw:-3.25542044639587,bn:11.1733026504517,be:1.19178116321564,bs:4.73672246932983},
	GN: {nc:'324',lc:'GIN',cn:'Conakry',cc:'Africa',sn:'Guinea',lm:'Conakry Grand Mosque',bw:-14.9266204833984,bn:12.6762218475342,be:-7.64107036590576,bs:7.19355249404907},
	//GW: position
	CI: {nc:'384',lc:'CIV',cn:'Yamoussoukro',cc:'Africa',sn:'Ivory Coast',lm:'Basilica Notre Dame de la Paix',bw:-8.59930324554443,bn:10.7366437911987,be:-2.49489665031433,bs:4.35706615447998},
	KE: {nc:'404',lc:'KEN',cn:'Nairobi',cc:'Africa',sn:'Kenya',lm:'Mount Kenya',bw:33.9088516235352,bn:5.01993894577026,be:41.8990821838379,bs:-4.67804765701294},
	LS: {nc:'462',lc:'LSO',cn:'Maseru',cc:'Africa',sn:'Lesotho',lm:'Maletsunyane Falls',bw:27.0290660858154,bn:-28.5720558166504,be:29.465763092041,bs:-30.668966293335},
	LR: {nc:'430',lc:'LBR',cn:'Monrovia',cc:'Africa',sn:'Liberia',lm:'Bomi County',bw:-11.4920845031738,bn:8.55179214477539,be:-7.3651123046875,bs:4.35305643081665},
	LY: {nc:'434',lc:'LBY',cn:'Tripoli',cc:'Africa',sn:'Libya',lm:'Ubari Oasis',bw:9.38701820373535,bn:33.1690063476562,be:25.1506156921387,bs:19.5080413818359},
	MG: {nc:'450',lc:'MDG',cn:'Antananarivo',cc:'Africa',sn:'Madagascar',lm:'Avenue of the Baobabs',bw:43.2248687744141,bn:-11.9454317092896,be:50.4837875366211,bs:-25.6089553833008},
	MW: {nc:'454',lc:'MWI',cn:'Lilongwe',cc:'Africa',sn:'Malawi',lm:'Lake Malawi',bw:32.673942565918,bn:-9.36753940582275,be:35.9168281555176,bs:-17.1250019073486},
	ML: {nc:'466',lc:'MLI',cn:'Bamako',cc:'Africa',sn:'Mali',lm:'Timbuktu',bw:-12.2426156997681,bn:25.0000057220459,be:4.2449688911438,bs:10.1595115661621},
	MR: {nc:'478',lc:'MRT',cn:'Nouakchott',cc:'Africa',sn:'Mauritania',lm:'Chinguetti Mosque',bw:-17.0665245056152,bn:27.2980766296387,be:-4.82767343521118,bs:14.7155456542969},
	MA: {nc:'504',lc:'MAR',cn:'Rabat',cc:'Africa',sn:'Morocco',lm:'King Hassan II Mosque',bw:-13.1685876846313,bn:35.9280319213867,be:-0.991749882698059,bs:27.6621112823486},
	MZ: {nc:'508',lc:'MOZ',cn:'Maputo',cc:'Africa',sn:'Mozambique',lm:'Mount Murresse',bw:30.2173156738281,bn:-10.4718818664551,be:40.8430023193359,bs:-26.868688583374},
	NA: {nc:'516',lc:'NAM',cn:'Windhoek',cc:'Africa',sn:'Namibia',lm:'Kalahari Desert',bw:11.7156286239624,bn:-16.9598903656006,be:25.2567043304443,bs:-28.9714336395264},
	NE: {nc:'562',lc:'NER',cn:'Niamey',cc:'Africa',sn:'Niger',lm:'Yaama Mosque',bw:0.166249975562096,bn:23.5250282287598,be:15.995644569397,bs:11.6969738006592},
	NG: {nc:'566',lc:'NGA',cn:'Abuja',cc:'Africa',sn:'Nigeria',lm:'Zuma Rock',bw:2.66843175888062,bn:13.8920087814331,be:14.6800746917725,bs:4.27714347839355},
	RW: {nc:'646',lc:'RWA',cn:'Kigali',cc:'Africa',sn:'Rwanda',lm:'Mount Karisimbi',bw:28.8567905426025,bn:-1.05348086357117,be:30.8959617614746,bs:-2.84067940711975},
BI: {nc:'108',lc:'BDI',cn:'Bujumbura',cc:'Africa',sn:'Burundi',lm:'Mausoleum of Prince Louis Rwagasore',bw:28.9930572509766,bn:-2.31012272834778,be:30.8477325439453,bs:-4.46571350097656},
	SN: {nc:'686',lc:'SEN',cn:'Dakar',cc:'Africa',sn:'Senegal',lm:'Maison des Esclaves',bw:-17.5352382659912,bn:16.6916351318359,be:-11.3558855056763,bs:12.3072738647461},
GM: {nc:'270',lc:'GMB',cn:'Banjul',cc:'Africa',sn:'Gambia',lm:'Arch 22 Monument',bw:-16.8250827789307,bn:13.8265724182129,be:-13.7977914810181,bs:13.0642509460449},
GW: {nc:'624',lc:'GNB',cn:'Bissau',cc:'Africa',sn:'Guinea-Bissau',lm:'Bissau Monument',bw:-16.7175369262695,bn:12.6807909011841,be:-13.6365203857422,bs:10.9242639541626},
	SL: {nc:'694',lc:'SLE',cn:'Freetown',cc:'Africa',sn:'Sierra Leone',lm:'Cotton Tree',bw:-13.3076324462891,bn:10.0000009536743,be:-10.284236907959,bs:6.92961025238037},
	SO: {nc:'706',lc:'SOM',cn:'Mogadishu',cc:'Africa',sn:'Somalia',lm:'Cal Madow Mountain',bw:40.9865875244141,bn:11.9791669845581,be:51.4126434326172,bs:-1.67486822605133},
	ZA: {nc:'710',lc:'ZAF',cn:'Tshwane/Pretoria',cc:'Africa',sn:'South Africa',lm:'Kruger National Park',bw:16.4580173492432,bn:-22.1266098022461,be:32.8959770202637,bs:-34.8398323059082},
	SD: {nc:'736',lc:'SDN',cn:'Khartoum',cc:'Africa',sn:'Sudan',lm:'Jebel Barkal',bw:21.8389434814453,bn:23.1468925476074,be:38.5800361633301,bs:3.48638963699341},
	SZ: {nc:'748',lc:'SWZ',cn:'Mbabane',cc:'Africa',sn:'Swaziland',lm:'Executioners Rock',bw:30.7941036224365,bn:-25.7196445465088,be:32.137264251709,bs:-27.3171043395996},
	TZ: {nc:'834',lc:'TZA',cn:'Dodoma',cc:'Africa',sn:'Tanzania',lm:'Mount Kilimanjaro',bw:29.3271656036377,bn:-0.99073588848114,be:40.4432258605957,bs:-11.7456970214844},
	TG: {nc:'768',lc:'TGO',cn:'Lome',cc:'Africa',sn:'Togo',lm:'Cadeao',bw:-0.147324025630951,bn:11.1389780044556,be:1.80669319629669,bs:6.10441637039185},
	TN: {nc:'788',lc:'TUN',cn:'Tunis',cc:'Africa',sn:'Tunisia',lm:'El-Djem',bw:7.52483224868774,bn:37.5439224243164,be:11.5982789993286,bs:30.2404136657715},
	UG: {nc:'800',lc:'UGA',cn:'Kampala',cc:'Africa',sn:'Uganda',lm:'Rwenzori Mountains',bw:29.5732498168945,bn:4.21442794799805,be:35.0360565185547,bs:-1.48405015468597},
	EH: {nc:'732',lc:'ESH',cn:'El Aaiún',cc:'Africa',sn:'Western Sahara',lm:'El Mchaouar square',bw:-17.1031856536865,bn:27.669677734375,be:-8.67027473449707,bs:20.7741546630859},
	ZM: {nc:'894',lc:'ZMB',cn:'Lusaka',cc:'Africa',sn:'Zambia',lm:'Victoria Falls',bw:21.9993686676025,bn:-8.22435855865479,be:33.7057113647461,bs:-18.079475402832},
	ZW: {nc:'716',lc:'ZWE',cn:'Harare',cc:'Africa',sn:'Zimbabwe',lm:'Mana Pools National Park',bw:25.237024307251,bn:-15.6088333129883,be:33.0563125610352,bs:-22.4177417755127}
};