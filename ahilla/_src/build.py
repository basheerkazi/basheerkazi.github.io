#!/usr/bin/env python3
"""Builds the AHILLA site in three languages from index.en.html.

    python3 ahilla/_src/build.py

Writes ahilla/index.html (English), ahilla/hi/index.html and ahilla/ur/index.html.
Edit index.en.html and the table below, then run this again. Folders starting
with _ are not published by GitHub Pages, so this script and the source stay
private to the repo. Every English string must be found in the source, or the
build stops, so a changed sentence can't silently stay untranslated.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
SITE = HERE.parent
SRC = (HERE / "index.en.html").read_text(encoding="utf-8")

# (English, Hindi, Urdu). Longer strings are replaced first.
T = [
    # head
    ("<title>AHILLA · The Islamic calendar that starts your day at Maghrib</title>",
     "<title>AHILLA · इस्लामी कैलेंडर जिसका दिन मग़रिब से शुरू होता है</title>",
     "<title>AHILLA · اسلامی کیلنڈر جس کا دن مغرب سے شروع ہوتا ہے</title>"),
    ('content="AHILLA is an Islamic calendar app for Indian Muslim families: Hijri dates from your moon committee, prayer start and end times, Ramadan countdown, 99 duas with a tasbih, and family dates. English, Hindi and Urdu. Coming to Google Play in January 2027."',
     'content="AHILLA भारत के मुस्लिम परिवारों के लिए इस्लामी कैलेंडर ऐप है: आपकी चाँद कमेटी की हिजरी तारीख़ें, नमाज़ के शुरू और ख़त्म होने का वक़्त, रमज़ान की उलटी गिनती, 99 दुआएँ और तस्बीह। अंग्रेज़ी, हिंदी और उर्दू में। जनवरी 2027 में Google Play पर।"',
     'content="AHILLA ہندوستان کے مسلم خاندانوں کے لیے اسلامی کیلنڈر ایپ ہے: آپ کی رؤیت ہلال کمیٹی کی ہجری تاریخیں، نماز کے شروع اور ختم ہونے کا وقت، رمضان کی الٹی گنتی، 99 دعائیں اور تسبیح۔ انگریزی، ہندی اور اردو میں۔ جنوری 2027 میں Google Play پر۔"'),

    # nav
    (">Features<", ">ख़ूबियाँ<", ">خوبیاں<"),
    (">Ramadan 2027<", ">रमज़ान 2027<", ">رمضان 2027<"),
    (">Downloads<", ">डाउनलोड<", ">ڈاؤن لوڈ<"),
    (">Feedback<", ">राय दें<", ">رائے دیں<"),
    (">Try it early<", ">पहले आज़माएँ<", ">پہلے آزمائیں<"),

    # hero
    ("Coming to Google Play · January 2027", "जनवरी 2027 में Google Play पर", "جنوری 2027 میں Google Play پر"),
    ("The Islamic calendar that starts your day at <em>Maghrib</em>",
     "वह इस्लामी कैलेंडर जिसका दिन <em>मग़रिब</em> से शुरू होता है",
     "وہ اسلامی کیلنڈر جس کا دن <em>مغرب</em> سے شروع ہوتا ہے"),
    ("Prayer times with start and end, your moon committee's dates, Ramadan made easy, 99 duas with a tasbih, and your family's dates. In one calm app made for Indian Muslim families.",
     "नमाज़ का शुरू और ख़त्म होने का वक़्त, आपकी चाँद कमेटी की तारीख़ें, आसान रमज़ान, तस्बीह के साथ 99 दुआएँ और आपके परिवार की तारीख़ें। भारत के मुस्लिम परिवारों के लिए बना एक सुकून भरा ऐप।",
     "نماز کے شروع اور ختم ہونے کا وقت، آپ کی رؤیت ہلال کمیٹی کی تاریخیں، آسان رمضان، تسبیح کے ساتھ 99 دعائیں اور آپ کے خاندان کی تاریخیں۔ ہندوستان کے مسلم خاندانوں کے لیے بنی ایک پُرسکون ایپ۔"),
    (">Join the early testers<", ">शुरुआती टेस्टर बनें<", ">ابتدائی ٹیسٹر بنیں<"),
    (">Free Moon Calendar 2027<", ">मुफ़्त चाँद कैलेंडर 2027<", ">مفت چاند کیلنڈر 2027<"),

    # six USPs
    ("Why AHILLA is different", "AHILLA अलग क्यों है", "AHILLA مختلف کیوں ہے"),
    ("Six things an ordinary calendar can't do", "छह काम जो आम कैलेंडर नहीं कर सकता", "چھ کام جو عام کیلنڈر نہیں کر سکتا"),
    ("Your day begins at Maghrib", "आपका दिन मग़रिब से शुरू होता है", "آپ کا دن مغرب سے شروع ہوتا ہے"),
    ("The Hijri date turns at sunset, the way the Islamic day really works.",
     "हिजरी तारीख़ सूरज डूबने पर बदलती है, जैसे इस्लामी दिन सच में चलता है।",
     "ہجری تاریخ غروبِ آفتاب پر بدلتی ہے، جیسے اسلامی دن واقعی چلتا ہے۔"),
    ("<b>Your moon committee</b>", "<b>आपकी चाँद कमेटी</b>", "<b>آپ کی رؤیت ہلال کمیٹی</b>"),
    ("Pick the committee your masjid follows. Dates update when they announce.",
     "वह कमेटी चुनें जिसे आपकी मस्जिद मानती है। ऐलान होते ही तारीख़ें बदल जाती हैं।",
     "وہ کمیٹی چنیں جسے آپ کی مسجد مانتی ہے۔ اعلان ہوتے ہی تاریخیں بدل جاتی ہیں۔"),
    ("Ramadan, made easy", "आसान रमज़ान", "آسان رمضان"),
    ("Countdown, sehri and iftar reminders, fast tracker and a Qur'an khatam plan.",
     "उलटी गिनती, सहरी और इफ़्तार की याद, रोज़ों का हिसाब और क़ुरआन ख़त्म का प्लान।",
     "الٹی گنتی، سحری اور افطار کی یاد دہانی، روزوں کا حساب اور ختمِ قرآن کا منصوبہ۔"),
    ("99 duas and a tasbih", "99 दुआएँ और तस्बीह", "99 دعائیں اور تسبیح"),
    ("Duas for every moment, in the order of Masnoon Duain, with references.",
     "हर मौक़े की दुआ, मसनून दुआएँ की तरतीब पर, हवालों के साथ।",
     "ہر موقع کی دعا، مسنون دعائیں کی ترتیب پر، حوالوں کے ساتھ۔"),
    ("Alerts that care", "फ़िक्र करने वाले अलर्ट", "فکر کرنے والے الرٹ"),
    ("Every prayer's start and end time, and a gentle nudge before it ends.",
     "हर नमाज़ के शुरू और ख़त्म होने का वक़्त, और ख़त्म होने से पहले एक नरम याद।",
     "ہر نماز کے شروع اور ختم ہونے کا وقت، اور ختم ہونے سے پہلے ایک نرم یاد دہانی۔"),
    ("Made for families", "परिवारों के लिए", "خاندانوں کے لیے"),
    ("Shared Family Wall, Hijri birthdays and a qaza tracker. In three languages.",
     "साझा फ़ैमिली वॉल, हिजरी सालगिरह और क़ज़ा का हिसाब। तीन ज़ुबानों में।",
     "مشترکہ فیملی وال، ہجری سالگرہ اور قضا کا حساب۔ تین زبانوں میں۔"),

    # Day Ring
    ("The Sunset Day Ring", "सनसेट डे रिंग", "سن سیٹ ڈے رِنگ"),
    ("Your whole Islamic day at a glance", "आपका पूरा इस्लामी दिन, एक नज़र में", "آپ کا پورا اسلامی دن، ایک نظر میں"),
    ("The day drawn as a ring from Maghrib to Maghrib, with every prayer on it.",
     "मग़रिब से मग़रिब तक का दिन एक रिंग में, हर नमाज़ के साथ।",
     "مغرب سے مغرب تک کا دن ایک دائرے میں، ہر نماز کے ساتھ۔"),
    ("A gold dot shows where you are now. The centre counts down to the next prayer.",
     "सुनहरा बिंदु बताता है कि आप अभी कहाँ हैं। बीच में अगली नमाज़ की उलटी गिनती।",
     "سنہرا نقطہ بتاتا ہے کہ آپ ابھی کہاں ہیں۔ بیچ میں اگلی نماز کی الٹی گنتی۔"),
    ("Each prayer's start and end time. Red marks show when not to pray.",
     "हर नमाज़ का शुरू और ख़त्म होने का वक़्त। लाल निशान बताते हैं कब नमाज़ नहीं पढ़नी।",
     "ہر نماز کے شروع اور ختم ہونے کا وقت۔ سرخ نشان بتاتے ہیں کب نماز نہیں پڑھنی۔"),
    ("Travelling? Times follow you to the new city by themselves.",
     "सफ़र में हैं? नए शहर के औक़ात ख़ुद आ जाते हैं।",
     "سفر میں ہیں؟ نئے شہر کے اوقات خود آ جاتے ہیں۔"),

    # Moon
    ("Moon sighting, done right", "चाँद देखना, सही तरीक़े से", "رؤیتِ ہلال، صحیح طریقے سے"),
    ("Your committee. Your dates.", "आपकी कमेटी। आपकी तारीख़ें।", "آپ کی کمیٹی۔ آپ کی تاریخیں۔"),
    ("Choose the moon committee your masjid follows. When they announce, AHILLA updates your calendar, reminders and home-screen widget by itself.",
     "वह चाँद कमेटी चुनें जिसे आपकी मस्जिद मानती है। उनके ऐलान पर AHILLA आपका कैलेंडर, याद दिलाने वाले अलर्ट और होम-स्क्रीन विजेट ख़ुद अपडेट कर देता है।",
     "وہ رؤیت ہلال کمیٹی چنیں جسے آپ کی مسجد مانتی ہے۔ ان کے اعلان پر AHILLA آپ کا کیلنڈر، یاد دہانیاں اور ہوم اسکرین وجٹ خود اپ ڈیٹ کر دیتا ہے۔"),
    ("Until they announce, dates come from a moon prediction for India: the crescent checked at sunset from eight cities, Mumbai to Kolkata.",
     "ऐलान होने तक तारीख़ें भारत के लिए चाँद के अंदाज़े से आती हैं: मुंबई से कोलकाता तक आठ शहरों में सूरज डूबने पर हिलाल की जाँच।",
     "اعلان ہونے تک تاریخیں ہندوستان کے لیے چاند کے اندازے سے آتی ہیں: ممبئی سے کولکاتا تک آٹھ شہروں میں غروب کے وقت ہلال کی جانچ۔"),
    ("On the 29th evening, Moon Watch tells you where and when to look.",
     "29 की शाम मून वॉच बताता है कि कहाँ और कब देखें।",
     "29 کی شام مون واچ بتاتا ہے کہ کہاں اور کب دیکھیں۔"),
    ("Saw the moon? Share your sighting with your committee in one tap.",
     "चाँद देखा? एक टैप में अपनी कमेटी को ख़बर भेजें।",
     "چاند دیکھا؟ ایک ٹیپ میں اپنی کمیٹی کو خبر بھیجیں۔"),

    # Dua
    ("Dua and Tasbih", "दुआ और तस्बीह", "دعا اور تسبیح"),
    ("A dua for every moment of the day", "दिन के हर पल की दुआ", "دن کے ہر لمحے کی دعا"),
    ("99 duas in 13 collections, arranged after <i>Masnoon Duain</i> by Maulana Ashiq Ilahi Bulandshahri (rahimahullah). Each one has the Arabic, its pronunciation, the meaning in three languages and its hadith reference.",
     "13 हिस्सों में 99 दुआएँ, मौलाना आशिक़ इलाही बुलंदशहरी (रहिमहुल्लाह) की <i>मसनून दुआएँ</i> की तरतीब पर। हर दुआ के साथ अरबी, उच्चारण, तीन ज़ुबानों में मतलब और हदीस का हवाला।",
     "13 حصوں میں 99 دعائیں، مولانا عاشق الٰہی بلند شہریؒ کی <i>مسنون دعائیں</i> کی ترتیب پر۔ ہر دعا کے ساتھ عربی، تلفظ، تین زبانوں میں مطلب اور حدیث کا حوالہ۔"),
    ("Subah Shaam ke Azkar with a counter on every dua.", "सुबह शाम के अज़कार, हर दुआ पर गिनती के साथ।", "صبح شام کے اذکار، ہر دعا پر گنتی کے ساتھ۔"),
    ("Namaz, safar, khana, shifa, barish and more. Manzil in full.",
     "नमाज़, सफ़र, खाना, शिफ़ा, बारिश और बहुत कुछ। पूरी मंज़िल।",
     "نماز، سفر، کھانا، شفا، بارش اور بہت کچھ۔ مکمل منزل۔"),
    ("A tasbih counter: tap anywhere and feel each count.",
     "तस्बीह काउंटर: कहीं भी टैप करें और हर गिनती महसूस करें।",
     "تسبیح کاؤنٹر: کہیں بھی ٹیپ کریں اور ہر گنتی محسوس کریں۔"),
    ("Reviewed by scholars before release.", "जारी करने से पहले उलमा की जाँच।", "جاری کرنے سے پہلے علماء کی جانچ۔"),
    ('aria-label="Try the tasbih: tap to count"', 'aria-label="तस्बीह आज़माएँ: गिनने के लिए टैप करें"', 'aria-label="تسبیح آزمائیں: گننے کے لیے ٹیپ کریں"'),
    ("Tap to try · 0 of 33", "आज़माने के लिए टैप करें · 33 में से 0", "آزمانے کے لیے ٹیپ کریں · 33 میں سے 0"),
    ("'Alhamdulillah, one round done' : 'Tap to try · ' + n + ' of 33'",
     "'अलहम्दुलिल्लाह, एक दौर पूरा' : 'आज़माने के लिए टैप करें · 33 में से ' + n",
     "'الحمدللہ، ایک دور مکمل' : 'آزمانے کے لیے ٹیپ کریں · 33 میں سے ' + n"),

    # Alerts and family
    ("Alerts and family", "अलर्ट और परिवार", "الرٹ اور خاندان"),
    ("A gentle nudge, never a nag", "नरम याद, कभी परेशानी नहीं", "نرم یاد دہانی، کبھی پریشانی نہیں"),
    ("An alert when each prayer time begins.", "हर नमाज़ का वक़्त शुरू होने पर अलर्ट।", "ہر نماز کا وقت شروع ہونے پر الرٹ۔"),
    ('About 20 minutes before Fajr, Zuhr, Asr or Maghrib ends: "still time to pray". Tap Prayed on the first alert and the nudge is skipped.',
     'फ़ज्र, ज़ुहर, अस्र या मग़रिब ख़त्म होने से लगभग 20 मिनट पहले: "अभी वक़्त है"। पहले अलर्ट पर "पढ़ ली" दबाएँ, तो यह याद नहीं आएगी।',
     'فجر، ظہر، عصر یا مغرب ختم ہونے سے تقریباً 20 منٹ پہلے: "ابھی وقت ہے"۔ پہلے الرٹ پر "پڑھ لی" دبائیں تو یہ یاد دہانی نہیں آئے گی۔'),
    ("Jumu'ah reminder on Friday morning.", "जुमे की सुबह जुमा की याद।", "جمعہ کی صبح جمعہ کی یاد دہانی۔"),
    ("Family Wall: one shared calendar for the whole family. Hijri birthdays, aqiqah and anniversaries.",
     "फ़ैमिली वॉल: पूरे परिवार का एक साझा कैलेंडर। हिजरी सालगिरह, अक़ीक़ा और बरसी।",
     "فیملی وال: پورے خاندان کا ایک مشترکہ کیلنڈر۔ ہجری سالگرہ، عقیقہ اور برسی۔"),
    ("Qaza ledger for missed prayers and fasts, made up step by step.",
     "छूटी नमाज़ों और रोज़ों का क़ज़ा हिसाब, क़दम ब क़दम पूरा करने के लिए।",
     "چھوٹی نمازوں اور روزوں کا قضا حساب، قدم بہ قدم پورا کرنے کے لیے۔"),

    # Ramadan
    ("Ramadan 2027 is coming", "रमज़ान 2027 आ रहा है", "رمضان 2027 آ رہا ہے"),
    (">Ramadan 1448<", ">रमज़ान 1448<", ">رمضان 1448<"),
    ('Expected to begin on <b style="color:#fff">Tuesday 9 February 2027</b> in India. The first taraweeh is on the evening of Monday 8 February.',
     'भारत में <b style="color:#fff">मंगल, 9 फ़रवरी 2027</b> से शुरू होने की उम्मीद। पहली तरावीह सोमवार 8 फ़रवरी की शाम।',
     'ہندوستان میں <b style="color:#fff">منگل، 9 فروری 2027</b> سے شروع ہونے کی امید۔ پہلی تراویح پیر 8 فروری کی شام۔'),
    ("<span>days</span>", "<span>दिन</span>", "<span>دن</span>"),
    ("<span>hours</span>", "<span>घंटे</span>", "<span>گھنٹے</span>"),
    ("<span>minutes</span>", "<span>मिनट</span>", "<span>منٹ</span>"),
    ("<span>seconds</span>", "<span>सेकंड</span>", "<span>سیکنڈ</span>"),
    ("Counting to Maghrib in Pune on 8 February. Confirm with your moon committee.",
     "8 फ़रवरी को पुणे के मग़रिब तक की गिनती। अपनी चाँद कमेटी से पुष्टि करें।",
     "8 فروری کو پونے کے مغرب تک کی گنتی۔ اپنی رؤیت ہلال کمیٹی سے تصدیق کریں۔"),
    ("<b>Shab-e-Barat</b>Night of Sat 23 Jan<br><small>15 Sha'ban</small>",
     "<b>शब-ए-बरात</b>शनि 23 जनवरी की रात<br><small>15 शाबान</small>",
     "<b>شبِ برات</b>ہفتہ 23 جنوری کی رات<br><small>15 شعبان</small>"),
    ("<b>First fast</b>Tue 9 Feb<br><small>1 Ramadan</small>",
     "<b>पहला रोज़ा</b>मंगल 9 फ़रवरी<br><small>1 रमज़ान</small>",
     "<b>پہلا روزہ</b>منگل 9 فروری<br><small>1 رمضان</small>"),
    ("<b>Laylat al-Qadr (27th night)</b>Night of Sat 6 Mar<br><small>Seek it in all odd nights</small>",
     "<b>शब-ए-क़द्र (27वीं रात)</b>शनि 6 मार्च की रात<br><small>सभी ताक़ रातों में तलाश करें</small>",
     "<b>شبِ قدر (ستائیسویں رات)</b>ہفتہ 6 مارچ کی رات<br><small>تمام طاق راتوں میں تلاش کریں</small>"),
    ("<b>Eid al-Fitr</b>Wed 10 Mar<br><small>1 Shawwal</small>",
     "<b>ईद उल-फ़ित्र</b>बुध 10 मार्च<br><small>1 शव्वाल</small>",
     "<b>عید الفطر</b>بدھ 10 مارچ<br><small>1 شوال</small>"),

    # Downloads
    ("Free to download and share", "मुफ़्त डाउनलोड करें और शेयर करें", "مفت ڈاؤن لوڈ کریں اور شیئر کریں"),
    ("Print them, forward them, put them up in your masjid.", "प्रिंट करें, आगे भेजें, अपनी मस्जिद में लगाएँ।", "پرنٹ کریں، آگے بھیجیں، اپنی مسجد میں لگائیں۔"),
    ("<b>Moon Calendar 2027 for India</b>", "<b>भारत के लिए चाँद कैलेंडर 2027</b>", "<b>ہندوستان کے لیے چاند کیلنڈر 2027</b>"),
    ("Every month of 2027 with Hijri dates, key Islamic days and a moon watch for eight Indian cities on each 29th evening.",
     "2027 का हर महीना हिजरी तारीख़ों, ख़ास इस्लामी दिनों और हर 29 की शाम भारत के आठ शहरों के चाँद के अंदाज़े के साथ।",
     "2027 کا ہر مہینہ ہجری تاریخوں، خاص اسلامی دنوں اور ہر 29 کی شام ہندوستان کے آٹھ شہروں کے چاند کے اندازے کے ساتھ۔"),
    ("PDF · 16 pages · A4 · 0.7 MB", "PDF · 16 पन्ने · A4 · 0.7 MB · अंग्रेज़ी में", "PDF · 16 صفحات · A4 · 0.7 MB · انگریزی میں"),
    ("<b>Introducing AHILLA</b>", "<b>AHILLA का परिचय</b>", "<b>AHILLA کا تعارف</b>"),
    ("The app in nine pages, with screenshots. Good for sharing with your family and masjid group.",
     "नौ पन्नों में ऐप, स्क्रीनशॉट के साथ। परिवार और मस्जिद ग्रुप में शेयर करने के लिए।",
     "نو صفحات میں ایپ، اسکرین شاٹس کے ساتھ۔ خاندان اور مسجد گروپ میں شیئر کرنے کے لیے۔"),
    ("PDF · 9 pages · 2 MB", "PDF · 9 पन्ने · 2 MB · अंग्रेज़ी में", "PDF · 9 صفحات · 2 MB · انگریزی میں"),
    (">Download</a>", ">डाउनलोड</a>", ">ڈاؤن لوڈ</a>"),
    ("<b>Hijri dates in your calendar</b>", "<b>हिजरी तारीख़ें आपके कैलेंडर में</b>", "<b>ہجری تاریخیں آپ کے کیلنڈر میں</b>"),
    ("Add Hijri dates to Google Calendar, Outlook or your iPhone. They update when committees announce.",
     "Google Calendar, Outlook या iPhone में हिजरी तारीख़ें जोड़ें। कमेटी के ऐलान पर ये अपडेट हो जाती हैं।",
     "Google Calendar، Outlook یا iPhone میں ہجری تاریخیں شامل کریں۔ کمیٹی کے اعلان پر یہ اپ ڈیٹ ہو جاتی ہیں۔"),
    ("Calendar feed (.ics)", "कैलेंडर फ़ीड (.ics)", "کیلنڈر فیڈ (.ics)"),
    (">Add to Google Calendar<", ">Google Calendar में जोड़ें<", ">Google Calendar میں شامل کریں<"),
    (">Other calendar apps<", ">दूसरे कैलेंडर ऐप<", ">دوسری کیلنڈر ایپس<"),
    ("<small>HIJRI DATES</small>", "<small>हिजरी तारीख़ें</small>", "<small>ہجری تاریخیں</small>"),

    # testers
    ("Be among the first families", "पहले परिवारों में शामिल हों", "پہلے خاندانوں میں شامل ہوں"),
    ("Try AHILLA before everyone else", "सबसे पहले AHILLA आज़माएँ", "سب سے پہلے AHILLA آزمائیں"),
    ("Early testing on Android starts on 9 December 2026, before the Play Store launch in January.",
     "Android पर शुरुआती टेस्टिंग 9 दिसंबर 2026 से, जनवरी में Play Store लॉन्च से पहले।",
     "Android پر ابتدائی ٹیسٹنگ 9 دسمبر 2026 سے، جنوری میں Play Store لانچ سے پہلے۔"),
    ("Email the Gmail ID that's on your Android phone to ",
     "अपने Android फ़ोन वाली Gmail ID ईमेल करें: ",
     "اپنے Android فون والی Gmail ID ای میل کریں: "),
    ("We send you a link to install it from Google Play.", "हम आपको Google Play से इंस्टॉल करने का लिंक भेजेंगे।", "ہم آپ کو Google Play سے انسٹال کرنے کا لنک بھیجیں گے۔"),
    ("Use it for a week and tell us what you think, with one tap in the app.",
     "एक हफ़्ता इस्तेमाल करें और ऐप में एक टैप से अपनी राय बताएँ।",
     "ایک ہفتہ استعمال کریں اور ایپ میں ایک ٹیپ سے اپنی رائے بتائیں۔"),
    (">Email my Gmail ID<", ">अपनी Gmail ID भेजें<", ">اپنی Gmail ID بھیجیں<"),
    (">Share on WhatsApp<", ">WhatsApp पर शेयर करें<", ">WhatsApp پر شیئر کریں<"),
    ("No ads. No sign-up needed in the app.", "कोई विज्ञापन नहीं। ऐप में साइन-अप की ज़रूरत नहीं।", "کوئی اشتہار نہیں۔ ایپ میں سائن اپ کی ضرورت نہیں۔"),

    # feedback
    ("Tell us what you think", "हमें अपनी राय बताएँ", "ہمیں اپنی رائے بتائیں"),
    ("Using AHILLA already? The quickest way is the row of faces at the bottom of Today, or More, then Send feedback. Or write here.",
     "AHILLA इस्तेमाल कर रहे हैं? सबसे आसान तरीक़ा: Today के नीचे चेहरों वाली लाइन, या More में Send feedback। या यहाँ लिखें।",
     "AHILLA استعمال کر رہے ہیں؟ سب سے آسان طریقہ: Today کے نیچے چہروں والی قطار، یا More میں Send feedback۔ یا یہاں لکھیں۔"),
    (">How is AHILLA for you?<", ">AHILLA आपको कैसा लगा?<", ">AHILLA آپ کو کیسا لگا؟<"),
    ('<label for="topic">About</label>', '<label for="topic">किस बारे में</label>', '<label for="topic">کس بارے میں</label>'),
    ("<option>General</option><option>Something broke</option><option>Prayer times</option>",
     "<option>आम बात</option><option>कुछ ख़राब है</option><option>नमाज़ के वक़्त</option>",
     "<option>عام بات</option><option>کچھ خراب ہے</option><option>نماز کے اوقات</option>"),
    ("<option>Moon dates</option><option>Duas</option><option>Language</option>",
     "<option>चाँद की तारीख़ें</option><option>दुआएँ</option><option>भाषा</option>",
     "<option>چاند کی تاریخیں</option><option>دعائیں</option><option>زبان</option>"),
    ("<option>An idea</option><option>Masjid or committee</option>",
     "<option>एक सुझाव</option><option>मस्जिद या कमेटी</option>",
     "<option>ایک تجویز</option><option>مسجد یا کمیٹی</option>"),
    ('<label for="msg">Your message</label>', '<label for="msg">आपका पैग़ाम</label>', '<label for="msg">آپ کا پیغام</label>'),
    ('placeholder="Anything you want to tell us"', 'placeholder="जो भी बताना चाहें"', 'placeholder="جو بھی بتانا چاہیں"'),
    ('type="submit">Send</button>', 'type="submit">भेजें</button>', 'type="submit">بھیجیں</button>'),
    ("This opens your email app with the message ready to send. Nothing is stored on this site.",
     "इससे आपका ईमेल ऐप तैयार पैग़ाम के साथ खुलेगा। इस साइट पर कुछ भी सेव नहीं होता।",
     "اس سے آپ کی ای میل ایپ تیار پیغام کے ساتھ کھلے گی۔ اس سائٹ پر کچھ بھی محفوظ نہیں ہوتا۔"),
    ('title="Very unhappy"', 'title="बहुत नाख़ुश"', 'title="بہت ناخوش"'),
    ('title="Unhappy"', 'title="नाख़ुश"', 'title="ناخوش"'),
    ('title="Okay"', 'title="ठीक है"', 'title="ٹھیک ہے"'),
    ('title="Happy"', 'title="ख़ुश"', 'title="خوش"'),
    ('title="Love it"', 'title="बहुत पसंद"', 'title="بہت پسند"'),

    # FAQ
    (">Questions<", ">सवाल<", ">سوالات<"),
    ("Frequently asked", "अक्सर पूछे जाने वाले सवाल", "اکثر پوچھے جانے والے سوالات"),
    ("Is AHILLA free?", "क्या AHILLA मुफ़्त है?", "کیا AHILLA مفت ہے؟"),
    ("Yes, AHILLA is free to download, with no ads.", "हाँ, AHILLA डाउनलोड करना मुफ़्त है, और कोई विज्ञापन नहीं।", "جی ہاں، AHILLA ڈاؤن لوڈ کرنا مفت ہے، اور کوئی اشتہار نہیں۔"),
    ("Which moon committee does it follow?", "यह किस चाँद कमेटी को मानता है?", "یہ کس رؤیت ہلال کمیٹی کو مانتا ہے؟"),
    ("The one you choose. Pick the committee your masjid follows, and AHILLA uses their announcements. Until they announce, it shows a moon prediction for India, and you can also shift dates by a day yourself in Settings.",
     "जिसे आप चुनें। वह कमेटी चुनें जिसे आपकी मस्जिद मानती है, AHILLA उनके ऐलान पर चलेगा। ऐलान होने तक यह भारत के लिए चाँद का अंदाज़ा दिखाता है, और Settings में आप ख़ुद भी तारीख़ एक दिन आगे-पीछे कर सकते हैं।",
     "جسے آپ چنیں۔ وہ کمیٹی چنیں جسے آپ کی مسجد مانتی ہے، AHILLA ان کے اعلان پر چلے گا۔ اعلان ہونے تک یہ ہندوستان کے لیے چاند کا اندازہ دکھاتا ہے، اور Settings میں آپ خود بھی تاریخ ایک دن آگے پیچھے کر سکتے ہیں۔"),
    ("Are the dates in the Moon Calendar final?", "क्या चाँद कैलेंडर की तारीख़ें पक्की हैं?", "کیا چاند کیلنڈر کی تاریخیں حتمی ہیں؟"),
    ("No. They are predictions from astronomy. Begin your fasts and Eid only after your moon committee announces. Dates in your area may differ by a day, and Kerala sometimes begins a day apart from the north.",
     "नहीं। ये खगोल विज्ञान पर आधारित अंदाज़े हैं। रोज़े और ईद अपनी चाँद कमेटी के ऐलान के बाद ही शुरू करें। आपके इलाक़े में तारीख़ एक दिन अलग हो सकती है, और केरल कभी-कभी उत्तर भारत से एक दिन अलग होता है।",
     "نہیں۔ یہ فلکیات پر مبنی اندازے ہیں۔ روزے اور عید اپنی رؤیت ہلال کمیٹی کے اعلان کے بعد ہی شروع کریں۔ آپ کے علاقے میں تاریخ ایک دن مختلف ہو سکتی ہے، اور کیرالا کبھی کبھی شمالی ہند سے ایک دن الگ ہوتا ہے۔"),
    ("Does it need an account? What about my data?", "क्या अकाउंट चाहिए? मेरे डेटा का क्या?", "کیا اکاؤنٹ چاہیے؟ میرے ڈیٹا کا کیا؟"),
    ('No account and no sign-up. Prayer times, fasts and duas stay on your phone. Only what you choose to share leaves it, such as Family Wall dates or feedback. Read the <a href="privacy.html">privacy policy</a>.',
     'न अकाउंट, न साइन-अप। नमाज़ के वक़्त, रोज़े और दुआएँ आपके फ़ोन में रहते हैं। सिर्फ़ वही बाहर जाता है जो आप ख़ुद शेयर करें, जैसे फ़ैमिली वॉल की तारीख़ें या आपकी राय। <a href="privacy.html">प्राइवेसी पॉलिसी</a> (अंग्रेज़ी में) पढ़ें।',
     'نہ اکاؤنٹ، نہ سائن اپ۔ نماز کے اوقات، روزے اور دعائیں آپ کے فون میں رہتی ہیں۔ صرف وہی باہر جاتا ہے جو آپ خود شیئر کریں، جیسے فیملی وال کی تاریخیں یا آپ کی رائے۔ <a href="privacy.html">پرائیویسی پالیسی</a> (انگریزی میں) پڑھیں۔'),
    ("Does it work offline?", "क्या यह बिना इंटरनेट चलता है?", "کیا یہ انٹرنیٹ کے بغیر چلتی ہے؟"),
    ("Yes. Prayer times, the calendar, duas and the tasbih all work without internet. It goes online to fetch moon announcements and for Family Wall.",
     "हाँ। नमाज़ के वक़्त, कैलेंडर, दुआएँ और तस्बीह बिना इंटरनेट चलते हैं। चाँद के ऐलान और फ़ैमिली वॉल के लिए इंटरनेट लगता है।",
     "جی ہاں۔ نماز کے اوقات، کیلنڈر، دعائیں اور تسبیح انٹرنیٹ کے بغیر چلتے ہیں۔ چاند کے اعلان اور فیملی وال کے لیے انٹرنیٹ چاہیے۔"),
    ("Is there an iPhone version?", "क्या iPhone के लिए है?", "کیا iPhone کے لیے ہے؟"),
    ("Not yet. AHILLA is for Android first. The Hijri calendar feed above works on iPhone today.",
     "अभी नहीं। AHILLA पहले Android के लिए है। ऊपर वाली हिजरी कैलेंडर फ़ीड iPhone पर आज भी चलती है।",
     "ابھی نہیں۔ AHILLA پہلے Android کے لیے ہے۔ اوپر والی ہجری کیلنڈر فیڈ iPhone پر آج بھی چلتی ہے۔"),
    ("Can my masjid work with AHILLA?", "क्या मेरी मस्जिद AHILLA के साथ जुड़ सकती है?", "کیا میری مسجد AHILLA کے ساتھ جڑ سکتی ہے؟"),
    ("Yes, please write to ", "जी हाँ, हमें लिखें: ", "جی ہاں، ہمیں لکھیں: "),
    (". We are starting with masjids in Pune.", "। हम पुणे की मस्जिदों से शुरुआत कर रहे हैं।", "۔ ہم پونے کی مساجد سے شروعات کر رہے ہیں۔"),

    # footer
    (" · Made in Pune", " · पुणे में बना", " · پونے میں بنا"),
    (">Privacy<", ">प्राइवेसी<", ">پرائیویسی<"),
    (">Terms<", ">शर्तें<", ">شرائط<"),

    # WhatsApp share text
    ("'Assalamu alaikum. AHILLA is a new Islamic calendar app for Indian Muslim families: prayer start and end times, ' +\n  'your moon committee\\'s dates, Ramadan countdown, 99 duas with a tasbih. In English, Hindi and Urdu. ' +\n  'Free Moon Calendar 2027 and early access here: https://basheerkazi.github.io/ahilla/'",
     "'अस्सलामु अलैकुम। AHILLA भारत के मुस्लिम परिवारों के लिए नया इस्लामी कैलेंडर ऐप है: नमाज़ के शुरू और ख़त्म होने का वक़्त, ' +\n  'आपकी चाँद कमेटी की तारीख़ें, रमज़ान की उलटी गिनती, तस्बीह के साथ 99 दुआएँ। हिंदी, उर्दू और अंग्रेज़ी में। ' +\n  'मुफ़्त चाँद कैलेंडर 2027 और पहले इस्तेमाल का मौक़ा: https://basheerkazi.github.io/ahilla/hi/'",
     "'السلام علیکم۔ AHILLA ہندوستان کے مسلم خاندانوں کے لیے نئی اسلامی کیلنڈر ایپ ہے: نماز کے شروع اور ختم ہونے کا وقت، ' +\n  'آپ کی رؤیت ہلال کمیٹی کی تاریخیں، رمضان کی الٹی گنتی، تسبیح کے ساتھ 99 دعائیں۔ اردو، ہندی اور انگریزی میں۔ ' +\n  'مفت چاند کیلنڈر 2027 اور پہلے استعمال کا موقع: https://basheerkazi.github.io/ahilla/ur/'"),
]

UR_CSS = """
/* Urdu: right to left, Nastaliq */
body { font-family:'Noto Nastaliq Urdu', Poppins, serif; line-height:2.1; }
h1, h2, h3, .usp b, .card b { line-height:1.9; }
.hero h1 { font-size:clamp(1.8rem,4.2vw,2.9rem); }
h2 { font-size:clamp(1.4rem,2.9vw,2rem); }
.kicker { letter-spacing:0; text-transform:none; font-size:.9rem; }
.count span { letter-spacing:0; }
.feature li { padding-left:0; padding-right:28px; }
.feature li::before { left:auto; right:4px; top:1.1em; }
.steps li { padding-left:0; padding-right:40px; }
.steps li::before { left:auto; right:0; }
summary::after { float:left; }
footer .ar { margin-left:0; margin-right:auto; }
.phones .phone:first-child { transform:translate(-40px,40px) rotate(6deg); }
.phones .phone:last-child { transform:translate(40px,0); }
.count, .lsw, .langs, .dl .meta { direction:ltr; }
.count { flex-direction:row-reverse; }
nav .links a, .btn, .lsw a { font-family:'Noto Nastaliq Urdu', Poppins, serif; }
"""

HI_CSS = """
/* Hindi: a touch more line height for Devanagari */
body { line-height:1.75; }
.kicker { letter-spacing:.04em; }
"""


def build(lang):
    s = SRC
    prefix = "" if lang == "en" else "../"
    links = {"@EN@": f"{prefix}./" if lang == "en" else "../",
             "@HI@": "hi/" if lang == "en" else ("./" if lang == "hi" else "../hi/"),
             "@UR@": "ur/" if lang == "en" else ("./" if lang == "ur" else "../ur/")}
    links["@EN@"] = "./" if lang == "en" else "../"
    for k, v in links.items():
        s = s.replace(k, v)
    for code in ("EN", "HI", "UR"):
        s = s.replace(f" @CUR_{code}@", ' aria-current="page"' if code.lower() == lang else "")
    if lang == "en":
        return s
    i = 1 if lang == "hi" else 2
    missing = []
    for row in sorted(T, key=lambda r: -len(r[0])):
        if row[0] not in s:
            missing.append(row[0][:70])
            continue
        s = s.replace(row[0], row[i])
    if missing:
        sys.exit("Not found in index.en.html (update the table):\n  " + "\n  ".join(missing))
    s = s.replace('<html lang="en">', f'<html lang="{lang}"' + (' dir="rtl">' if lang == "ur" else ">"))
    s = s.replace("</style>", (UR_CSS if lang == "ur" else HI_CSS) + "</style>", 1)
    s = s.replace('content="https://basheerkazi.github.io/ahilla/"', f'content="https://basheerkazi.github.io/ahilla/{lang}/"')
    # assets live one folder up
    for a in ('src="img/', 'href="img/', 'href="downloads/', 'href="privacy.html', 'href="terms.html'):
        s = s.replace(a, a.replace('="', '="../'))
    return s


for lang, out in (("en", SITE / "index.html"), ("hi", SITE / "hi" / "index.html"), ("ur", SITE / "ur" / "index.html")):
    out.parent.mkdir(exist_ok=True)
    out.write_text(build(lang), encoding="utf-8")
    print("wrote", out.relative_to(SITE.parent))
