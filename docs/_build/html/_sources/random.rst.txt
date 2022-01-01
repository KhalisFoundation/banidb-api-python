Random
------

Get Random Shabad for specific source.

.. code:: python

   banidb.random(source_id='G')

**Parameters**

-  `source_id <sources>`__ *(str)*: from where you want to the ang (by
   default, **G** for Guru Granth Sahib Ji).

**Returns**: Search Results as dictionary(key-value pair).

**Return type**: dict

Example
^^^^^^^

.. code:: python

   # Searching Bandhana Har Bandhana Gun Gaavo Gopal Rai....
   shabad_data = banidb.random()
   print(shabad_data)

**Output**

.. code:: json

   {
       'shabad_id': 5213, 
       'source_uni': 'ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ', 
       'source_eng': 'Sri Guru Granth Sahib Ji', 
       'writer': 'Bhagat Sheikh Fareed Ji', 
       'ang': 1378, 
       'verses': 
           [{
           'verse_id': 58548, 
           'verse': 'ਕਿਝੁ ਨ ਬੁਝੈ ਕਿਝੁ ਨ ਸੁਝੈ ਦੁਨੀਆ ਗੁਝੀ ਭਾਹਿ ॥',
           'steek':{
               'en': {
                   'bdb': 'I know nothing; I understand nothing. The world is a smouldering fire.', 
                   'ms': 'I see nothing and know nothing, as the world is a smoldering fire.', 
                   'ssk': 'I know nothing; I understand nothing. The world is a smouldering fire.'
               }, 
               'pu': {
                   'ss': {
                       'gurmukhi': 'dunIAw lukvIN A`g hY ,kuJ sUJ-bUJ nhIN pYNdI [', 
                       'unicode': 'ਦੁਨੀਆ ਲੁਕਵੀਂ ਅੱਗ ਹੈ ,ਕੁਝ ਸੂਝ-ਬੂਝ ਨਹੀਂ ਪੈਂਦੀ ।'
                   }, 
                   'ft': {
                       'gurmukhi': 'ies dunIAW ko kuC Drm kI bUJ nhIN hY AOr Apny srUp kI kuC sUJ nhIN[ iesI kr ky sMpUrn dunIAW ko AwSw iqRSnw rUp guJI AgnI lwg rhI hY]',
                       'unicode': 'ਇਸ ਦੁਨੀਆਂ ਕੋ ਕੁਛ ਧਰਮ ਕੀ ਬੂਝ ਨਹੀਂ ਹੈ ਔਰ ਅਪਨੇ ਸਰੂਪ ਕੀ ਕੁਛ ਸੂਝ ਨਹੀਂ। ਇਸੀ ਕਰ ਕੇ ਸੰਪੂਰਨ ਦੁਨੀਆਂ ਕੋ ਆਸ਼ਾ ਤ੍ਰਿਸ਼ਨਾ ਰੂਪ ਗੁਝੀ ਅਗਨੀ ਲਾਗ ਰਹੀ ਹੈ॥'
                   }, 
                   'bdb': {
                       'gurmukhi': 'dunIAw lukvIN A`g hY ,kuJ sUJ-bUJ nhIN pYNdI [',
                       'unicode': 'ਦੁਨੀਆ ਲੁਕਵੀਂ ਅੱਗ ਹੈ ,ਕੁਝ ਸੂਝ-ਬੂਝ ਨਹੀਂ ਪੈਂਦੀ ।'
                   }, 
                   'ms': {
                       'gurmukhi': 'mYN kuC nhIN sI jwxdw, mYƒ kuC BI nhIN idsdw, ikauN ik sMswr sulGdI hoeI A`g hY[', 
                       'unicode': 'ਮੈਂ ਕੁਛ ਨਹੀਂ ਸੀ ਜਾਣਦਾ, ਮੈਨੂੰ ਕੁਛ ਭੀ ਨਹੀਂ ਦਿਸਦਾ, ਕਿਉਂ ਕਿ ਸੰਸਾਰ ਸੁਲਘਦੀ ਹੋਈ ਅੱਗ ਹੈ।'
                   }
               }, 
               'es': {
                   'sn': 'No sé nada, no entiendo nada, el mundo es una bola de fuego, '
               }, 
               'hi': {
                   'ss': 'दुनिया (देखने में तो गुलज़ार है। पर इसका मोह असल में) छुपी हुई गुप्त आग है (जो अंदर ही अंदर मन में धुखती रहती है; इसमें पड़े हुए जीवों को जिंदगी के सही रास्ते की) कुछ सूझ-बूझ नहीं पड़ती।',
                   'sts': 'यह दुनिया छिपी हुई आग है, जिसमें कुछ समझ नहीं आता।'
               }
           }, 
           'transliteration': {
               'english': 'kijh na bujhai kijh na sujhai dhuneeaa gujhee bhaeh ||',
               'hindi': 'किझु न बुझै किझु न सुझै दुनीआ गुझी भाहि ॥',
               'en': 'kijh na bujhai kijh na sujhai dhuneeaa gujhee bhaeh ||', 
               'hi': 'किझु न बुझै किझु न सुझै दुनीआ गुझी भाहि ॥',
               'ipa': 'kɪɖ͡ʐ nə bʊɖ͡ʐæ kɪɖ͡ʐ nə sʊɖ͡ʐæ d̪ʊniəɑ Gʊɖ͡ʐi ɓɑh.',
               'ur': 'کِجھ ن بُجھَے کجھ ن سُجھَے دُنیِآ گُجھیِ بھاه ۔۔'
           }
       }, 
       {
           'verse_id': 58549, 
           'verse': 'ਸਾਂਈਂ ਮੇਰੈ ਚੰਗਾ ਕੀਤਾ ਨਾਹੀ ਤ ਹੰ ਭੀ ਦਝਾਂ ਆਹਿ ॥੩॥', 
           'steek': {
               'en': {
                   'bdb': 'My Lord did well to warn me about it; otherwise, I would have been burnt as well. ||3||', 
                   'ms': 'My Lord did well to warn me, otherwise, I too would have been burnt.', 
                   'ssk': 'My Lord did well to warn me about it; otherwise, I would have been burnt as well. ||3||'
               }, 
               'pu': {
                   'ss': {
                       'gurmukhi': ' myry sWeI ny (myry auqy) myhr kIqI hY ,nhIN qW (bwkI lokW vWg) mYN BI (ies ivc) sV jWdw [3[', 
                       'unicode': ' ਮੇਰੇ ਸਾਂਈ ਨੇ (ਮੇਰੇ ਉਤੇ) ਮੇਹਰ ਕੀਤੀ ਹੈ ,ਨਹੀਂ ਤਾਂ (ਬਾਕੀ ਲੋਕਾਂ ਵਾਂਗ) ਮੈਂ ਭੀ (ਇਸ ਵਿਚ) ਸੜ ਜਾਂਦਾ ।੩।'
                   },
                   'ft': {
                       'gurmukhi': 'qW qy myry sweIN ny myry swQ cMgw kIqw hY, jo ies gRhsq qy muJ ko bcwie lIAw hY[ nhIN qo mYN BI iesI pRkwr ies AgnI myN (dJW) dgD hoxw sI]3]ÇPrId jI AYsy kih kr iqs Kyq vwly ko khw: qUM jwh qyry KrbUjy ausI qrh ho jwvyNgy[ qb iqs ny pUCw: ieh ikAw cirqR hUAw hY[ qo PrId jI ny khw: ausI Kyq myN eyk isr rih jwvygw, quJ ko au`qR dyvygw[ qb vhu AYsy sun kr jb Awkr dyKy qo sBI KrbUjy ho gey hYN[ voh jo eyk isr pVw Qw iqs ko pUCw, qb voh hsw BI AO roXw BI[ qo iqs ny iqs sy hsny AO rony kw kwrn pUCw, qb Eh isr kihqw BXw: hy ABwgy purS! hm cOrwsI myN Brmqy hUey Ab ies jnm myN Awey Qy[ jykr hmwry bIc sy eyk BI aun sMqoN ky ArQ lg jwqw qb hm sBI mukiq ho jwqy[ ies kr ky qo mYN hsw Qw[ prMqU qYny sMqoN kw svwl nhIN mwnw[ hm iqn ky ArQ n Awvny sy Pyr cOrwsI myN hI rih gey, XW qy mYN roXw hUM[ iqs isr sy AYsy bcn sun kr auh gRhsqI BI veIrwg krdy bMdgI krny lwgw]',
                       'unicode': 'ਤਾਂ ਤੇ ਮੇਰੇ ਸਾਈਂ ਨੇ ਮੇਰੇ ਸਾਥ ਚੰਗਾ ਕੀਤਾ ਹੈ, ਜੋ ਇਸ ਗ੍ਰਹਸਤ ਤੇ ਮੁਝ ਕੋ ਬਚਾਇ ਲੀਆ ਹੈ। ਨਹੀਂ ਤੋ ਮੈਂ ਭੀ ਇਸੀ ਪ੍ਰਕਾਰ ਇਸ ਅਗਨੀ ਮੇਂ (ਦਝਾਂ) ਦਗਧ ਹੋਣਾ ਸੀ॥੩॥☬ਫਰੀਦ ਜੀ ਐਸੇ ਕਹਿ ਕਰ ਤਿਸ ਖੇਤ ਵਾਲੇ ਕੋ ਕਹਾ: ਤੂੰ ਜਾਹ ਤੇਰੇ ਖਰਬੂਜੇ ਉਸੀ ਤਰਹ ਹੋ ਜਾਵੇਂਗੇ। ਤਬ ਤਿਸ ਨੇ ਪੂਛਾ: ਇਹ ਕਿਆ ਚਰਿਤ੍ਰ ਹੂਆ ਹੈ। ਤੋ ਫਰੀਦ ਜੀ ਨੇ ਕਹਾ: ਉਸੀ ਖੇਤ ਮੇਂ ਏਕ ਸਿਰ ਰਹਿ ਜਾਵੇਗਾ, ਤੁਝ ਕੋ ਉੱਤ੍ਰ ਦੇਵੇਗਾ। ਤਬ ਵਹੁ ਐਸੇ ਸੁਨ ਕਰ ਜਬ ਆਕਰ ਦੇਖੇ ਤੋ ਸਭੀ ਖਰਬੂਜੇ ਹੋ ਗਏ ਹੈਂ। ਵੋਹ ਜੋ ਏਕ ਸਿਰ ਪੜਾ ਥਾ ਤਿਸ ਕੋ ਪੂਛਾ, ਤਬ ਵੋਹ ਹਸਾ ਭੀ ਔ ਰੋਯਾ ਭੀ। ਤੋ ਤਿਸ ਨੇ ਤਿਸ ਸੇ ਹਸਨੇ ਔ ਰੋਨੇ ਕਾ ਕਾਰਨ ਪੂਛਾ, ਤਬ ਓਹ ਸਿਰ ਕਹਿਤਾ ਭਯਾ: ਹੇ ਅਭਾਗੇ ਪੁਰਸ਼! ਹਮ ਚੌਰਾਸੀ ਮੇਂ ਭਰਮਤੇ ਹੂਏ ਅਬ ਇਸ ਜਨਮ ਮੇਂ ਆਏ ਥੇ। ਜੇਕਰ ਹਮਾਰੇ ਬੀਚ ਸੇ ਏਕ ਭੀ ਉਨ ਸੰਤੋਂ ਕੇ ਅਰਥ ਲਗ ਜਾਤਾ ਤਬ ਹਮ ਸਭੀ ਮੁਕਤਿ ਹੋ ਜਾਤੇ। ਇਸ ਕਰ ਕੇ ਤੋ ਮੈਂ ਹਸਾ ਥਾ। ਪਰੰਤੂ ਤੈਨੇ ਸੰਤੋਂ ਕਾ ਸਵਾਲ ਨਹੀਂ ਮਾਨਾ। ਹਮ ਤਿਨ ਕੇ ਅਰਥ ਨ ਆਵਨੇ ਸੇ ਫੇਰ ਚੌਰਾਸੀ ਮੇਂ ਹੀ ਰਹਿ ਗਏ, ਯਾਂ ਤੇ ਮੈਂ ਰੋਯਾ ਹੂੰ। ਤਿਸ ਸਿਰ ਸੇ ਐਸੇ ਬਚਨ ਸੁਨ ਕਰ ਉਹ ਗ੍ਰਹਸਤੀ ਭੀ ਵਈਰਾਗ ਕਰਦੇ ਬੰਦਗੀ ਕਰਨੇ ਲਾਗਾ॥'
                   }, 
                   'bdb': {
                       'gurmukhi': ' myry sWeI ny (myry auqy) myhr kIqI hY ,nhIN qW (bwkI lokW vWg) mYN BI (ies ivc) sV jWdw [3[', 
                       'unicode': ' ਮੇਰੇ ਸਾਂਈ ਨੇ (ਮੇਰੇ ਉਤੇ) ਮੇਹਰ ਕੀਤੀ ਹੈ ,ਨਹੀਂ ਤਾਂ (ਬਾਕੀ ਲੋਕਾਂ ਵਾਂਗ) ਮੈਂ ਭੀ (ਇਸ ਵਿਚ) ਸੜ ਜਾਂਦਾ ।੩।'
                   }, 
                   'ms': {
                       'gurmukhi': 'myry mwlk ny Blw kIqw ik mYƒ Kbrdwr kr id`qw, nhIN qW mYN BI sV bl jWdw[', 
                       'unicode': 'ਮੇਰੇ ਮਾਲਕ ਨੇ ਭਲਾ ਕੀਤਾ ਕਿ ਮੈਨੂੰ ਖਬਰਦਾਰ ਕਰ ਦਿੱਤਾ, ਨਹੀਂ ਤਾਂ ਮੈਂ ਭੀ ਸੜ ਬਲ ਜਾਂਦਾ।'
                   }
               }, 
               'es': {
                   'sn': 'mi Señor hizo bien en advertirme, de otra forma me hubiera quemado ahí también. (3)'
               }, 
               'hi': {
                   'ss': "मेरे सांई ने (मेरे ऊपर) मेहर की है (और मुझे इससे बचा लिया है) नहीं तो (बाकी लोगों की तरह) मैं भी (इसमें) जल जाता ( भाव। माया के मोह से प्रभू स्वयं ही मेहर करके बचाता है। हमारे अपने वश की बात नहीं कि यह 'पोटली' सिर से उतार के फेंक सकें)। 3।",
                   'sts': 'मेरे मालिक ने बहुत अच्छा किया, जो रहम करके मुझे इससे बचा लिया, अन्यथा मैंने भी इसमें जल जाना था ॥३॥'
               }
           }, 
           'transliteration': {
               'english': 'saa(n)iee(n) merai cha(n)gaa keetaa naahee ta ha(n) bhee dhajhaa(n) aaeh ||3||', 
               'hindi': 'साँईं मेरै चंगा कीता नाही त हं भी दझाँ आहि ॥३॥',
               'en': 'saa(n)iee(n) merai cha(n)gaa keetaa naahee ta ha(n) bhee dhajhaa(n) aaeh ||3||', 
               'hi': 'साँईं मेरै चंगा कीता नाही त हं भी दझाँ आहि ॥३॥',
               'ipa': 'sɑⁿeiⁿ meræ t͡ʃəŋGɑ kit̪ɑ nɑhi t̪ həŋ ɓi d̪əɖ͡ʐɑⁿ əɑh.3.',
               'ur': 'ساںایں مےرَے چںگا کیِتا ناهیِ ت هں بھیِ دجھاں آه ۔۔۳۔۔'
           }
       }]
   }
