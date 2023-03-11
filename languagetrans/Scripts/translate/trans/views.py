from django.shortcuts import render
from django.http import HttpResponse
import googletrans
# Create your views here.
d=googletrans.LANGUAGES
lst=list(d.values())
def index(request):
    return render(request,'index.html',{'lang':lst})
def speechpage(request):
    return render(request,'speechpage.html',{'lang':lst})
from googletrans import Translator
from gtts import gTTS
def translate(request):
    t=Translator()
    lst1=list(d.keys())
    ind=lst.index(str(request.GET['lang']))
    cod=lst[ind]
    global out
    source=t.detect(str(request.GET['inptext'])).lang
    out=t.translate(request.GET['inptext'],dest=cod)
    stri=out.text
    lst55=list(stri.split('\n'))
    stri=""
    for i in lst55:
        stri+=(" "+i.rstrip("\r"))
    print(lst55)
    print(stri)
    lst3=[
    "Microsoft David - English (United States)",
    "Microsoft Ravi - English (India)",
    "Microsoft Heera - English (India)",
    "Microsoft Mark - English (United States)",
    "Microsoft Zira - English (United States)",
    "Microsoft Adri Online (Natural) - Afrikaans (South Africa)",
    "Microsoft Willem Online (Natural) - Afrikaans (South Africa)",
    "Microsoft Anila Online (Natural) - Albanian (Albania)",
    "Microsoft Ilir Online (Natural) - Albanian (Albania)",
    "Microsoft Ameha Online (Natural) - Amharic (Ethiopia)",
    "Microsoft Mekdes Online (Natural) - Amharic (Ethiopia)",
    "Microsoft Amina Online (Natural) - Arabic (Algeria)",
    "Microsoft Ismael Online (Natural) - Arabic (Algeria)",
    "Microsoft Ali Online (Natural) - Arabic (Bahrain)",
    "Microsoft Laila Online (Natural) - Arabic (Bahrain)",
    "Microsoft Salma Online (Natural) - Arabic (Egypt)",
    "Microsoft Shakir Online (Natural) - Arabic (Egypt)",
    "Microsoft Bassel Online (Natural) - Arabic (Iraq)",
    "Microsoft Rana Online (Natural) - Arabic (Iraq)",
    "Microsoft Sana Online (Natural) - Arabic (Jordan)",
    "Microsoft Taim Online (Natural) - Arabic (Jordan)",
    "Microsoft Fahed Online (Natural) - Arabic (Kuwait)",
    "Microsoft Noura Online (Natural) - Arabic (Kuwait)",
    "Microsoft Layla Online (Natural) - Arabic (Lebanon)",
    "Microsoft Rami Online (Natural) - Arabic (Lebanon)",
    "Microsoft Iman Online (Natural) - Arabic (Libya)",
    "Microsoft Omar Online (Natural) - Arabic (Libya)",
    "Microsoft Jamal Online (Natural) - Arabic (Morocco)",
    "Microsoft Mouna Online (Natural) - Arabic (Morocco)",
    "Microsoft Abdullah Online (Natural) - Arabic (Oman)",
    "Microsoft Aysha Online (Natural) - Arabic (Oman)",
    "Microsoft Amal Online (Natural) - Arabic (Qatar)",
    "Microsoft Moaz Online (Natural) - Arabic (Qatar)",
    "Microsoft Hamed Online (Natural) - Arabic (Saudi Arabia)",
    "Microsoft Zariyah Online (Natural) - Arabic (Saudi Arabia)",
    "Microsoft Amany Online (Natural) - Arabic (Syria)",
    "Microsoft Laith Online (Natural) - Arabic (Syria)",
    "Microsoft Hedi Online (Natural) - Arabic (Tunisia)",
    "Microsoft Reem Online (Natural) - Arabic (Tunisia)",
    "Microsoft Fatima Online (Natural) - Arabic (United Arab Emirates)",
    "Microsoft Hamdan Online (Natural) - Arabic (United Arab Emirates)",
    "Microsoft Maryam Online (Natural) - Arabic (Yemen)",
    "Microsoft Saleh Online (Natural) - Arabic (Yemen)",
    "Microsoft Babek Online (Natural) - Azerbaijani (Azerbaijan)",
    "Microsoft Banu Online (Natural) - Azerbaijani (Azerbaijan)",
    "Microsoft Nabanita Online (Natural) - Bangla (Bangladesh)",
    "Microsoft Pradeep Online (Natural) - Bangla (Bangladesh)",
    "Microsoft Bashkar Online (Natural) - Bangla (India)",
    "Microsoft Tanishaa Online (Natural) - Bengali (India)",
    "Microsoft Goran Online (Natural) - Bosnian (Bosnia)",
    "Microsoft Vesna Online (Natural) - Bosnian (Bosnia)",
    "Microsoft Borislav Online (Natural) - Bulgarian (Bulgaria)",
    "Microsoft Kalina Online (Natural) - Bulgarian (Bulgaria)",
    "Microsoft Nilar Online (Natural) - Burmese (Myanmar)",
    "Microsoft Thiha Online (Natural) - Burmese (Myanmar)",
    "Microsoft Enric Online (Natural) - Catalan (Spain)",
    "Microsoft Joana Online (Natural) - Catalan (Spain)",
    "Microsoft HiuGaai Online (Natural) - Chinese (Cantonese Traditional)",
    "Microsoft HiuMaan Online (Natural) - Chinese (Hong Kong)",
    "Microsoft WanLung Online (Natural) - Chinese (Hong Kong)",
    "Microsoft Xiaoxiao Online (Natural) - Chinese (Mainland)",
    "Microsoft Xiaoyi Online (Natural) - Chinese (Mainland)",
    "Microsoft Yunjian Online (Natural) - Chinese (Mainland)",
    "Microsoft Yunxi Online (Natural) - Chinese (Mainland)",
    "Microsoft Yunxia Online (Natural) - Chinese (Mainland)",
    "Microsoft Yunyang Online (Natural) - Chinese (Mainland)",
    "Microsoft Xiaobei Online (Natural) - Chinese (Northeastern Mandarin)",
    "Microsoft HsiaoChen Online (Natural) - Chinese (Taiwan)",
    "Microsoft YunJhe Online (Natural) - Chinese (Taiwan)",
    "Microsoft HsiaoYu Online (Natural) - Chinese (Taiwanese Mandarin)",
    "Microsoft Xiaoni Online (Natural) - Chinese (Zhongyuan Mandarin Shaanxi)",
    "Microsoft Gabrijela Online (Natural) - Croatian (Croatia)",
    "Microsoft Srecko Online (Natural) - Croatian (Croatia)",
    "Microsoft Antonin Online (Natural) - Czech (Czech)",
    "Microsoft Vlasta Online (Natural) - Czech (Czech)",
    "Microsoft Christel Online (Natural) - Danish (Denmark)",
    "Microsoft Jeppe Online (Natural) - Danish (Denmark)",
    "Microsoft Arnaud Online (Natural) - Dutch (Belgium)",
    "Microsoft Dena Online (Natural) - Dutch (Belgium)",
    "Microsoft Colette Online (Natural) - Dutch (Netherlands)",
    "Microsoft Fenna Online (Natural) - Dutch (Netherlands)",
    "Microsoft Maarten Online (Natural) - Dutch (Netherlands)",
    "Microsoft Natasha Online (Natural) - English (Australia)",
    "Microsoft William Online (Natural) - English (Australia)",
    "Microsoft Clara Online (Natural) - English (Canada)",
    "Microsoft Liam Online (Natural) - English (Canada)",
    "Microsoft Sam Online (Natural) - English (Hongkong)",
    "Microsoft Yan Online (Natural) - English (Hongkong)",
    "Microsoft Neerja Online (Natural) - English (India) (Preview)",
    "Microsoft Neerja Online (Natural) - English (India)",
    "Microsoft Prabhat Online (Natural) - English (India)",
    "Microsoft Connor Online (Natural) - English (Ireland)",
    "Microsoft Emily Online (Natural) - English (Ireland)",
    "Microsoft Asilia Online (Natural) - English (Kenya)",
    "Microsoft Chilemba Online (Natural) - English (Kenya)",
    "Microsoft Mitchell Online (Natural) - English (New Zealand)",
    "Microsoft Molly Online (Natural) - English (New Zealand)",
    "Microsoft Abeo Online (Natural) - English (Nigeria)",
    "Microsoft Ezinne Online (Natural) - English (Nigeria)",
    "Microsoft James Online (Natural) - English (Philippines)",
    "Microsoft Rosa Online (Natural) - English (Philippines)",
    "Microsoft Luna Online (Natural) - English (Singapore)",
    "Microsoft Wayne Online (Natural) - English (Singapore)",
    "Microsoft Leah Online (Natural) - English (South Africa)",
    "Microsoft Luke Online (Natural) - English (South Africa)",
    "Microsoft Elimu Online (Natural) - English (Tanzania)",
    "Microsoft Imani Online (Natural) - English (Tanzania)",
    "Microsoft Libby Online (Natural) - English (United Kingdom)",
    "Microsoft Maisie Online (Natural) - English (United Kingdom)",
    "Microsoft Ryan Online (Natural) - English (United Kingdom)",
    "Microsoft Sonia Online (Natural) - English (United Kingdom)",
    "Microsoft Thomas Online (Natural) - English (United Kingdom)",
    "Microsoft Aria Online (Natural) - English (United States)",
    "Microsoft Ana Online (Natural) - English (United States)",
    "Microsoft Christopher Online (Natural) - English (United States)",
    "Microsoft Eric Online (Natural) - English (United States)",
    "Microsoft Guy Online (Natural) - English (United States)",
    "Microsoft Jenny Online (Natural) - English (United States)",
    "Microsoft Michelle Online (Natural) - English (United States)",
    "Microsoft Roger Online (Natural) - English (United States)",
    "Microsoft Steffan Online (Natural) - English (United States)",
    "Microsoft Anu Online (Natural) - Estonian (Estonia)",
    "Microsoft Kert Online (Natural) - Estonian (Estonia)",
    "Microsoft Angelo Online (Natural) - Filipino (Philippines)",
    "Microsoft Blessica Online (Natural) - Filipino (Philippines)",
    "Microsoft Harri Online (Natural) - Finnish (Finland)",
    "Microsoft Noora Online (Natural) - Finnish (Finland)",
    "Microsoft Charline Online (Natural) - French (Belgium)",
    "Microsoft Gerard Online (Natural) - French (Belgium)",
    "Microsoft Antoine Online (Natural) - French (Canada)",
    "Microsoft Jean Online (Natural) - French (Canada)",
    "Microsoft Sylvie Online (Natural) - French (Canada)",
    "Microsoft Denise Online (Natural) - French (France)",
    "Microsoft Eloise Online (Natural) - French (France)",
    "Microsoft Henri Online (Natural) - French (France)",
    "Microsoft Ariane Online (Natural) - French (Switzerland)",
    "Microsoft Fabrice Online (Natural) - French (Switzerland)",
    "Microsoft Roi Online (Natural) - Galician (Spain)",
    "Microsoft Sabela Online (Natural) - Galician (Spain)",
    "Microsoft Eka Online (Natural) - Georgian (Georgia)",
    "Microsoft Giorgi Online (Natural) - Georgian (Georgia)",
    "Microsoft Ingrid Online (Natural) - German (Austria)",
    "Microsoft Jonas Online (Natural) - German (Austria)",
    "Microsoft Amala Online (Natural) - German (Germany)",
    "Microsoft Conrad Online (Natural) - German (Germany)",
    "Microsoft Katja Online (Natural) - German (Germany)",
    "Microsoft Killian Online (Natural) - German (Germany)",
    "Microsoft Jan Online (Natural) - German (Switzerland)",
    "Microsoft Leni Online (Natural) - German (Switzerland)",
    "Microsoft Athina Online (Natural) - Greek (Greece)",
    "Microsoft Nestoras Online (Natural) - Greek (Greece)",
    "Microsoft Dhwani Online (Natural) - Gujarati (India)",
    "Microsoft Niranjan Online (Natural) - Gujarati (India)",
    "Microsoft Avri Online (Natural) - Hebrew (Israel)",
    "Microsoft Hila Online (Natural) - Hebrew (Israel)",
    "Microsoft Madhur Online (Natural) - Hindi (India)",
    "Microsoft Swara Online (Natural) - Hindi (India)",
    "Microsoft Noemi Online (Natural) - Hungarian (Hungary)",
    "Microsoft Tamas Online (Natural) - Hungarian (Hungary)",
    "Microsoft Gudrun Online (Natural) - Icelandic (Iceland)",
    "Microsoft Gunnar Online (Natural) - Icelandic (Iceland)",
    "Microsoft Ardi Online (Natural) - Indonesian (Indonesia)",
    "Microsoft Gadis Online (Natural) - Indonesian (Indonesia)",
    "Microsoft Colm Online (Natural) - Irish (Ireland)",
    "Microsoft Orla Online (Natural) - Irish (Ireland)",
    "Microsoft Diego Online (Natural) - Italian (Italy)",
    "Microsoft Elsa Online (Natural) - Italian (Italy)",
    "Microsoft Isabella Online (Natural) - Italian (Italy)",
    "Microsoft Keita Online (Natural) - Japanese (Japan)",
    "Microsoft Nanami Online (Natural) - Japanese (Japan)",
    "Microsoft Dimas Online (Natural) - Javanese (Indonesia)",
    "Microsoft Siti Online (Natural) - Javanese (Indonesia)",
    "Microsoft Gagan Online (Natural) - Kannada (India)",
    "Microsoft Sapna Online (Natural) - Kannada (India)",
    "Microsoft Aigul Online (Natural) - Kazakh (Kazakhstan)",
    "Microsoft Daulet Online (Natural) - Kazakh (Kazakhstan)",
    "Microsoft Piseth Online (Natural) - Khmer (Cambodia)",
    "Microsoft Sreymom Online (Natural) - Khmer (Cambodia)",
    "Microsoft InJoon Online (Natural) - Korean (Korea)",
    "Microsoft SunHi Online (Natural) - Korean (Korea)",
    "Microsoft Chanthavong Online (Natural) - Lao (Laos)",
    "Microsoft Keomany Online (Natural) - Lao (Laos)",
    "Microsoft Everita Online (Natural) - Latvian (Latvia)",
    "Microsoft Nils Online (Natural) - Latvian (Latvia)",
    "Microsoft Leonas Online (Natural) - Lithuanian (Lithuania)",
    "Microsoft Ona Online (Natural) - Lithuanian (Lithuania)",
    "Microsoft Aleksandar Online (Natural) - Macedonian (Republic of North Macedonia)",
    "Microsoft Marija Online (Natural) - Macedonian (Republic of North Macedonia)",
    "Microsoft Osman Online (Natural) - Malay (Malaysia)",
    "Microsoft Yasmin Online (Natural) - Malay (Malaysia)",
    "Microsoft Midhun Online (Natural) - Malayalam (India)",
    "Microsoft Sobhana Online (Natural) - Malayalam (India)",
    "Microsoft Grace Online (Natural) - Maltese (Malta)",
    "Microsoft Joseph Online (Natural) - Maltese (Malta)",
    "Microsoft Aarohi Online (Natural) - Marathi (India)",
    "Microsoft Manohar Online (Natural) - Marathi (India)",
    "Microsoft Bataa Online (Natural) - Mongolian (Mongolia)",
    "Microsoft Yesui Online (Natural) - Mongolian (Mongolia)",
    "Microsoft Hemkala Online (Natural) - Nepali (Nepal)",
    "Microsoft Sagar Online (Natural) - Nepali (Nepal)",
    "Microsoft Finn Online (Natural) - Norwegian (Bokmål Norway)",
    "Microsoft Pernille Online (Natural) - Norwegian (Bokmål, Norway)",
    "Microsoft GulNawaz Online (Natural) - Pashto (Afghanistan)",
    "Microsoft Latifa Online (Natural) - Pashto (Afghanistan)",
    "Microsoft Dilara Online (Natural) - Persian (Iran)",
    "Microsoft Farid Online (Natural) - Persian (Iran)",
    "Microsoft Marek Online (Natural) - Polish (Poland)",
    "Microsoft Zofia Online (Natural) - Polish (Poland)",
    "Microsoft Antonio Online (Natural) - Portuguese (Brazil)",
    "Microsoft Francisca Online (Natural) - Portuguese (Brazil)",
    "Microsoft Duarte Online (Natural) - Portuguese (Portugal)",
    "Microsoft Raquel Online (Natural) - Portuguese (Portugal)",
    "Microsoft Alina Online (Natural) - Romanian (Romania)",
    "Microsoft Emil Online (Natural) - Romanian (Romania)",
    "Microsoft Dmitry Online (Natural) - Russian (Russia)",
    "Microsoft Svetlana Online (Natural) - Russian (Russia)",
    "Microsoft Nicholas Online (Natural) - Serbian (Serbia)",
    "Microsoft Sophie Online (Natural) - Serbian (Serbia)",
    "Microsoft Sameera Online (Natural) - Sinhala (Sri Lanka)",
    "Microsoft Thilini Online (Natural) - Sinhala (Sri Lanka)",
    "Microsoft Lukas Online (Natural) - Slovak (Slovakia)",
    "Microsoft Viktoria Online (Natural) - Slovak (Slovakia)",
    "Microsoft Petra Online (Natural) - Slovenian (Slovenia)",
    "Microsoft Rok Online (Natural) - Slovenian (Slovenia)",
    "Microsoft Muuse Online (Natural) - Somali (Somalia)",
    "Microsoft Ubax Online (Natural) - Somali (Somalia)",
    "Microsoft Elena Online (Natural) - Spanish (Argentina)",
    "Microsoft Tomas Online (Natural) - Spanish (Argentina)",
    "Microsoft Marcelo Online (Natural) - Spanish (Bolivia)",
    "Microsoft Sofia Online (Natural) - Spanish (Bolivia)",
    "Microsoft Catalina Online (Natural) - Spanish (Chile)",
    "Microsoft Lorenzo Online (Natural) - Spanish (Chile)",
    "Microsoft Gonzalo Online (Natural) - Spanish (Colombia)",
    "Microsoft Salome Online (Natural) - Spanish (Colombia)",
    "Microsoft Juan Online (Natural) - Spanish (Costa Rica)",
    "Microsoft Maria Online (Natural) - Spanish (Costa Rica)",
    "Microsoft Belkys Online (Natural) - Spanish (Cuba)",
    "Microsoft Manuel Online (Natural) - Spanish (Cuba)",
    "Microsoft Emilio Online (Natural) - Spanish (Dominican Republic)",
    "Microsoft Ramona Online (Natural) - Spanish (Dominican Republic)",
    "Microsoft Andrea Online (Natural) - Spanish (Ecuador)",
    "Microsoft Luis Online (Natural) - Spanish (Ecuador)",
    "Microsoft Lorena Online (Natural) - Spanish (El Salvador)",
    "Microsoft Rodrigo Online (Natural) - Spanish (El Salvador)",
    "Microsoft Javier Online (Natural) - Spanish (Equatorial Guinea)",
    "Microsoft Teresa Online (Natural) - Spanish (Equatorial Guinea)",
    "Microsoft Andres Online (Natural) - Spanish (Guatemala)",
    "Microsoft Marta Online (Natural) - Spanish (Guatemala)",
    "Microsoft Carlos Online (Natural) - Spanish (Honduras)",
    "Microsoft Karla Online (Natural) - Spanish (Honduras)",
    "Microsoft Dalia Online (Natural) - Spanish (Mexico)",
    "Microsoft Jorge Online (Natural) - Spanish (Mexico)",
    "Microsoft LorenzoEsCL Online (Natural) - Spanish (Mexico)",
    "Microsoft Federico Online (Natural) - Spanish (Nicaragua)",
    "Microsoft Yolanda Online (Natural) - Spanish (Nicaragua)",
    "Microsoft Margarita Online (Natural) - Spanish (Panama)",
    "Microsoft Roberto Online (Natural) - Spanish (Panama)",
    "Microsoft Mario Online (Natural) - Spanish (Paraguay)",
    "Microsoft Tania Online (Natural) - Spanish (Paraguay)",
    "Microsoft Alex Online (Natural) - Spanish (Peru)",
    "Microsoft Camila Online (Natural) - Spanish (Peru)",
    "Microsoft Karina Online (Natural) - Spanish (Puerto Rico)",
    "Microsoft Victor Online (Natural) - Spanish (Puerto Rico)",
    "Microsoft Alvaro Online (Natural) - Spanish (Spain)",
    "Microsoft Elvira Online (Natural) - Spanish (Spain)",
    "Microsoft ManuelEsCU Online (Natural) - Spanish (Spain)",
    "Microsoft Alonso Online (Natural) - Spanish (United States)",
    "Microsoft Paloma Online (Natural) - Spanish (United States)",
    "Microsoft Mateo Online (Natural) - Spanish (Uruguay)",
    "Microsoft Valentina Online (Natural) - Spanish (Uruguay)",
    "Microsoft Paola Online (Natural) - Spanish (Venezuela)",
    "Microsoft Sebastian Online (Natural) - Spanish (Venezuela)",
    "Microsoft Jajang Online (Natural) - Sundanese (Indonesia)",
    "Microsoft Tuti Online (Natural) - Sundanese (Indonesia)",
    "Microsoft Rafiki Online (Natural) - Swahili (Kenya)",
    "Microsoft Zuri Online (Natural) - Swahili (Kenya)",
    "Microsoft Daudi Online (Natural) - Swahili (Tanzania)",
    "Microsoft Rehema Online (Natural) - Swahili (Tanzania)",
    "Microsoft Mattias Online (Natural) - Swedish (Sweden)",
    "Microsoft Sofie Online (Natural) - Swedish (Sweden)",
    "Microsoft Pallavi Online (Natural) - Tamil (India)",
    "Microsoft Valluvar Online (Natural) - Tamil (India)",
    "Microsoft Kani Online (Natural) - Tamil (Malaysia)",
    "Microsoft Surya Online (Natural) - Tamil (Malaysia)",
    "Microsoft Anbu Online (Natural) - Tamil (Singapore)",
    "Microsoft Venba Online (Natural) - Tamil (Singapore)",
    "Microsoft Kumar Online (Natural) - Tamil (Sri Lanka)",
    "Microsoft Saranya Online (Natural) - Tamil (Sri Lanka)",
    "Microsoft Mohan Online (Natural) - Telugu (India)",
    "Microsoft Shruti Online (Natural) - Telugu (India)",
    "Microsoft Niwat Online (Natural) - Thai (Thailand)",
    "Microsoft Premwadee Online (Natural) - Thai (Thailand)",
    "Microsoft Ahmet Online (Natural) - Turkish (Turkey)",
    "Microsoft Emel Online (Natural) - Turkish (Turkey)",
    "Microsoft Ostap Online (Natural) - Ukrainian (Ukraine)",
    "Microsoft Polina Online (Natural) - Ukrainian (Ukraine)",
    "Microsoft Gul Online (Natural) - Urdu (India)",
    "Microsoft Salman Online (Natural) - Urdu (India)",
    "Microsoft Asad Online (Natural) - Urdu (Pakistan)",
    "Microsoft Uzma Online (Natural) - Urdu (Pakistan)",
    "Microsoft Madina Online (Natural) - Uzbek (Uzbekistan)",
    "Microsoft Sardor Online (Natural) - Uzbek (Uzbekistan)",
    "Microsoft HoaiMy Online (Natural) - Vietnamese (Vietnam)",
    "Microsoft NamMinh Online (Natural) - Vietnamese (Vietnam)",
    "Microsoft Aled Online (Natural) - Welsh (United Kingdom)",
    "Microsoft Nia Online (Natural) - Welsh (United Kingdom)",
    "Microsoft Thando Online (Natural) - Zulu (South Africa)",
    "Microsoft Themba Online (Natural) - Zulu (South Africa)"
    ]
    lst4=[]
    des=str(request.GET['lang'])
    flag=False
    for i in lst3:
        if des.lower() in i.lower():
            lst4+=[i]
            flag=True
    outtxt=str(stri)
    outtxt=outtxt.replace(" ","_")
    prono=str(out.pronunciation)
    prono=prono.replace(" ","_")
    if not flag:
        lst4=["this language can't be spelled out as it is but you could try in other formats"]
    return render(request,'output.html',{'text':outtxt,'source':d[source],'destlanguage':request.GET['lang'],'destlang':lst4})
#import gtts
"""def speakspeech(request):
    lst1=list(d.keys())
    ind=lst.index(str(request.GET['destlangu']))
    cod=lst[ind]
    d2=gtts.lang.tts_langs()
    if cod in d2.keys():
        we=gTTS(text=request.GET['transtext'],lang=cod,slow=False)
    else:
        we=gTTS(text=request.GET['transtext'],lang='en',slow=False)
    we.save("del.wav")
    #playsound("del.wav")
    return render(request,"<audio src='del.wav' autoplay></audio>")"""
"""This application cant spell following languages
armenian
basque
belarusian
cebuano
chichewa
chinese (simplified)
chinese (traditional)
corsican
esperanto
frisian
haitian creole
hausa
hawaiian
hmong
igbo
kurdish (kurmanji)
kyrgyz
latin
luxembourgish
malagasy
maori
myanmar (burmese)
punjabi
samoan
scots gaelic
sesotho
shona
sindhi
tajik
uyghur
xhosa
yiddish
yoruba
But you could read them by text
"""