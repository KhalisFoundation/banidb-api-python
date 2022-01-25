Banis
-----

Get Sundar Gutka Bani Ids with Bani names.

.. code:: python

   banidb.banis()

Returns bani ids to be used in `bani <#bani>`__ to get specific bani.

**Returns**: Sundar Gutka Banis as dictionary(key-value pair).

**Return type**: dict

**Example**:

.. code:: python

   banis_data = banidb.banis()
   print(banis_data)

**Output**

.. code:: 

   {
      "1":{
         "gurmukhiUni":"ਗੁਰ ਮੰਤ੍ਰ",
         "transliterations":{
            "english":"gur ma(n)tr",
            "hindi":"गुर मंत्र",
            "en":"gur ma(n)tr",
            "hi":"गुर मंत्र",
            "ipa":"Gʊr məŋt̪ɹ",
            "ur":"گُر مںتر"
         }
      },
      "2":{
         "gurmukhiUni":"ਜਪੁਜੀ ਸਾਹਿਬ",
         "transliterations":{
            "english":"japujee saahib",
            "hindi":"जपुजी साहिब",
            "en":"japujee saahib",
            "hi":"जपुजी साहिब",
            "ipa":"d͡ʒəpʊd͡ʒi sɑhɪb",
            "ur":"جپجیِ ساهب"
         }
      }
      ...
   }

Bani
^^^^

Get Sundar Gutka Bani using Bani Id.

.. code:: python

   banidb.bani(bani_id, larivaar=False)

Returns bani from Sundar Gutka according to the given bani_id.

**Parameters:**

-  **bani_id** *(str or int)*: id of the specific bani, recieved from
   the `banis <banis.html>`__.
-  **larivaar** *(bool)*: you want it to be in larivaar or not.

**Returns**: Specific Sundar Gutka Bani as dictionary(key-value pair).

**Return type**: dict

**Example**:

.. code:: python

   bani_data = banidb.bani(10)
   print(bani_data)

**Output**

.. code:: 

   {
      "info":{
         "bani_id":10,
         "unicode":"ਅਨੰਦੁ ਸਾਹਿਬ",
         "english":"ana(n)dh saahib",
         "hindi":"अनंदु साहिब",
         "ipa":"ənəⁿd̪ sɑhɪb",
         "urdu":"انµد ساهب"
      },
      "raag":{
         "raagId":22,
         "gurmukhi":"rwgu rwmklI",
         "unicode":"ਰਾਗੁ ਰਾਮਕਲੀ",
         "english":"Raag Raamkalee",
         "raagWithPage":"Raamkalee (876-974)"
      },
      "source":{
         "sourceId":"G",
         "gurmukhi":"sRI gurU gRMQ swihb jI",
         "unicode":"ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ",
         "english":"Sri Guru Granth Sahib Ji",
         "pageNo":917
      },
      "verses":[
         {
            "verse_id":1783,
            "verse":"ੴ ਸਤਿਗੁਰ ਪ੍ਰਸਾਦਿ ॥",
            "steek":{
               "en":{
                  "bdb":"One Universal Creator God. By The Grace Of The True Guru:",
                  "ms":"There is but One God. By True Guru's grace, He is obtained.",
                  "ssk":"One Universal Creator God. By The Grace Of The True Guru:"
               },
               "pu":{
                  "ss":{
                     "gurmukhi":"None",
                     "unicode":"None"
                  },
                  "ft":{
                     "gurmukhi":"",
                     "unicode":""
                  },
                  "bdb":{
                     "gurmukhi":"None",
                     "unicode":"None"
                  },
                  "ms":{
                     "gurmukhi":"vwihgurU kyvl iek hY[ s¤cy gurW dI dieAw duAwrw auh pwieAw jWdw hY[",
                     "unicode":"ਵਾਹਿਗੁਰੂ ਕੇਵਲ ਇਕ ਹੈ। ਸੱਚੇ ਗੁਰਾਂ ਦੀ ਦਇਆ ਦੁਆਰਾ ਉਹ ਪਾਇਆ ਜਾਂਦਾ ਹੈ।"
                  }
               },
               "es":{
                  "sn":"Un Dios Creador del Universo, por la Gracia del Verdadero Guru"
               },
               "hi":{
                  
               }
            },
            "translit":{
               "english":"ikOankaar satigur prasaadh ||",
               "hindi":"ੴ सतिगुर प्रसादि ॥",
               "en":"ikOankaar satigur prasaadh ||",
               "hi":"ੴ सतिगुर प्रसादि ॥",
               "ipa":"ɪk oəŋkɑɾ sət̪ɪGʊr pɹəsɑd̪.",
               "ur":"اک اونکار ستگر پرساد ۔۔"
            }
         },
         {
            "verse_id":1784,
            "verse":"ਰਾਮਕਲੀ ਮਹਲਾ ੩ ਅਨੰਦੁ",
            "steek":{
               "en":{
                  "bdb":"Raamkalee, Third Mehla, Anand ~ The Song Of Bliss:",
                  "ms":"Ramkali 3rd Guru. Anand.",
                  "ssk":"Raamkalee, Third Mehl, Anand ~ The Song Of Bliss:"
               },
               "pu":{
                  "ss":{
                     "gurmukhi":"None",
                     "unicode":"None"
                  },
                  "ft":{
                     "gurmukhi":"",
                     "unicode":""
                  },
                  "bdb":{
                     "gurmukhi":"None",
                     "unicode":"None"
                  },
                  "ms":{
                     "gurmukhi":"rwmklI qIjI pwiqSwhI[ AMnd[",
                     "unicode":"ਰਾਮਕਲੀ ਤੀਜੀ ਪਾਤਿਸ਼ਾਹੀ। ਅੰਨਦ।"
                  }
               },
               "es":{
                  "sn":"Ramkali, Mejl Guru Amar Das, Tercer Canal Divino, Anand -La Melodía del Éxtasis."
               },
               "hi":{
                  
               }
            },
            "translit":{
               "english":"raamakalee mahalaa teejaa ana(n)dhu",
               "hindi":"रामकली महला ३ अनंदु",
               "en":"raamakalee mahalaa teejaa ana(n)dhu",
               "hi":"रामकली महला ३ अनंदु",
               "ipa":"rɑməkəli məhəlɑ t̪id͡ʒɑ ənəⁿd̪ʊ",
               "ur":"رامکلیِ مهلا ۳ انµد"
            }
         },
         ...
      ]
   }
