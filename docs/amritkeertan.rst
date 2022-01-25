Amrit Keertan
-------------

Get all Headers with Id from Amrit Keertan.

.. code:: python

   banidb.amritkeertan()

**Returns**: amrit keertan headers with header ids to be used in `amrit
keertan search <#amrit-keertan-search>`__ to read shabads.

**Return type**: list of dict

**Example**:

.. code:: python

   keertan_data = banidb.amritkeertan()
   print(keertan_data)

**Output**

.. code:: json

   [
      {
         "header_id":1,
         "gurmukhi_uni":"ਦੁਇ ਕਰ ਜੋੜਿ ਕਰਉ ਅਰਦਾਸਿ ॥",
         "gurmukhi":"duie kr joiV krau Ardwis ]",
         "translit":{
            "en":"dhui kar joR karau aradhaas ||",
            "hi":"दुइ कर जोड़ि करउ अरदासि ॥",
            "ipa":"d̪ʊeɪ kər d͡ʒɔɽ kəro ərəd̪ɑs.",
            "ur":"دُا کر جوڑ کرا ارداس ۔۔"
         }
      },
      {
         "header_id":2,
         "gurmukhi_uni":"ਢਾਢੀ ਕਰੈ ਪੁਕਾਰ ॥",
         "gurmukhi":"FwFI krY pukwr ]",
         "translit":{
            "en":"ddaaddee karai pukaar ||",
            "hi":"ढाढी करै पुकार ॥",
            "ipa":"ʈɑʈi kəræ pʊkɑr.",
            "ur":"ڈھاڈھیِ کرَے پُکار ۔۔"
         }
      },
      {
         "header_id":3,
         "gurmukhi_uni":"ਗੁਰਸਿਖਾਂ ਕੀ ਹਰਿ ਧੂੜਿ ਦੇਹਿ",
         "gurmukhi":"gurisKW kI hir DUiV dyih",
         "translit":{
            "en":"gursikhaa(n) kee har dhooR dheh",
            "hi":"गुरसिखाँ की हरि धूड़ि देहि",
            "ipa":"Gʊrəsɪkʰɑⁿ ki hər t̪uɽ d̪eh",
            "ur":"گُرسکھاں کیِ هر دھُوڑ دےه"
         }
      }
   ]

Amrit Keertan Search
^^^^^^^^^^^^^^^^^^^^

Get all available Shabad Indexes in the specific header of Amrit
Keertan.

.. code:: python

   banidb.amritkeertan_search(header_id)

**Parameters**:

-  **header_id** *(int)*: header id for Amrit Keertan.

**Returns**: available shabad indexes with shabad ids to get
`shabads <shabad.html>`__ in the specific header.

**Return type**: list of dict

**Example**:

.. code:: python

   keertan_data = banidb.amritkeertan_search(1)
   print(keertan_data)

**Output**:

.. code::

   {
      "header_id":1,
      "gurmukhi":"ਦੁਇ ਕਰ ਜੋੜਿ ਕਰਉ ਅਰਦਾਸਿ ॥",
      "translit":{
         "en":"dhui kar joR karau aradhaas ||",
         "hi":"दुइ कर जोड़ि करउ अरदासि ॥",
         "ipa":"d̪ʊeɪ kər d͡ʒɔɽ kəro ərəd̪ɑs.",
         "ur":"دُا کر جوڑ کرا ارداس ۔۔"
      },
      "banis":[
         {
            "index_id":1,
            "header_id":1,
            "shabad_id":816,
            "gurmukhi_uni":"ਡੰਡਉਤਿ ਬੰਦਨ ਅਨਿਕ ਬਾਰ ਸਰਬ ਕਲਾ ਸਮਰਥ ॥",
            "steek":{
               "en":{
                  "bdb":"I bow down, and fall to the ground in humble adoration, countless times, to the All-powerful Lord, who possesses all powers.",
                  "ms":"Prostrate salutation and obeisance I make many a time before the Omnipotent Lord the Possessor of all the powers.",
                  "ssk":"I bow down, and fall to the ground in humble adoration, countless times, to the All-powerful Lord, who possesses all powers."
               },
               "pu":{
                  "ss":"hy nwnk! (ieauN Ardws kr—) hy swrIAW qwkqW r`Kx vwly pRBU! mYN AnykW vwrI qYƒ nmskwr krdw hW [ ",
                  "ft":"hy srb klw SkqI kr smrQ vwihgurU! qyry ko (fMfauiq) dMfvq ho kr myrI Anyk vwr nmskwr hY]",
                  "bdb":"hy nwnk! (ieauN Ardws kr—) hy swrIAW qwkqW r`Kx vwly pRBU! mYN AnykW vwrI qYƒ nmskwr krdw hW [ ",
                  "ms":"mYN lMmy pY ky nmSkwr Aqy pRxwm, AnykW vwrI, swrIAW qwkqw vwly, srb-SkqIvwn suAwmI muhry, krdw hW["
               },
               "puu":{
                  "ss":"ਹੇ ਨਾਨਕ! (ਇਉਂ ਅਰਦਾਸ ਕਰ—) ਹੇ ਸਾਰੀਆਂ ਤਾਕਤਾਂ ਰੱਖਣ ਵਾਲੇ ਪ੍ਰਭੂ! ਮੈਂ ਅਨੇਕਾਂ ਵਾਰੀ ਤੈਨੂੰ ਨਮਸਕਾਰ ਕਰਦਾ ਹਾਂ । ",
                  "ft":"ਹੇ ਸਰਬ ਕਲਾ ਸ਼ਕਤੀ ਕਰ ਸਮਰਥ ਵਾਹਿਗੁਰੂ! ਤੇਰੇ ਕੋ (ਡੰਡਉਤਿ) ਦੰਡਵਤ ਹੋ ਕਰ ਮੇਰੀ ਅਨੇਕ ਵਾਰ ਨਮਸਕਾਰ ਹੈ॥",
                  "bdb":"ਹੇ ਨਾਨਕ! (ਇਉਂ ਅਰਦਾਸ ਕਰ—) ਹੇ ਸਾਰੀਆਂ ਤਾਕਤਾਂ ਰੱਖਣ ਵਾਲੇ ਪ੍ਰਭੂ! ਮੈਂ ਅਨੇਕਾਂ ਵਾਰੀ ਤੈਨੂੰ ਨਮਸਕਾਰ ਕਰਦਾ ਹਾਂ । ",
                  "ms":"ਮੈਂ ਲੰਮੇ ਪੈ ਕੇ ਨਮਸ਼ਕਾਰ ਅਤੇ ਪ੍ਰਣਾਮ, ਅਨੇਕਾਂ ਵਾਰੀ, ਸਾਰੀਆਂ ਤਾਕਤਾ ਵਾਲੇ, ਸਰਬ-ਸ਼ਕਤੀਵਾਨ ਸੁਆਮੀ ਮੁਹਰੇ, ਕਰਦਾ ਹਾਂ।"
               },
               "es":{
                  "sn":"Un millón de veces me postro ante Ti, Señor Todo Poderoso, "
               },
               "hi":{
                  "ss":"हे नानक ! (ऐसे अरदास कर-) हे सारी ताकतें रखने वाले प्रभू ! मैं अनेकों बार तुझे नमस्कार करता हूँ।",
                  "sts":"हे नानक ! (इस तरह वन्दना कर-) हे सर्वकला सम्पूर्ण प्रभु ! मैं अनेक बार तुझे प्रणाम करता हूँ।"
               }
            },
            "translit":{
               "en":"dda(n)ddaut ba(n)dhan anik baar sarab kalaa samarath ||",
               "hi":"डंडउति बंदन अनिक बार सरब कला समरथ ॥",
               "ipa":"ɖəŋɖoʊt̪ bəŋd̪ən ənɪk bɑr sərəb kəlɑ səmərət̪ʰ.",
               "ur":"ڈںڈات بںدن انک بار سرب کلا سمرتھ ۔۔"
            },
            "source_id":"G",
            "ang":256,
            "writer":"Guru Arjan Dev Ji",
            "raag_id":7
         }
         ...
      ]
   }
