Raags
-----

Get list of all available Raags.

.. code:: python

   banidb.raags()

**Returns**: Raags with Raag Ids(used in `raag <#raag>`__) as list of dictionaries.

**Return type**: list of dict

**Example**:

.. code:: python

   raags_data = banidb.raags()
   print(raags_data)

**Output**

.. code:: 

   [
      {
         "raag_id":5,
         "raag_uni":"ਸਿਰੀ ਰਾਗੁ",
         "raag_eng":"Siree Raag"
      },
      {
         "raag_id":6,
         "raag_uni":"ਰਾਗੁ ਮਾਝ",
         "raag_eng":"Raag Maajh"
      },
      {
         "raag_id":7,
         "raag_uni":"ਰਾਗੁ ਗਉੜੀ",
         "raag_eng":"Raag Gauree"
      },
      {
         "raag_id":8,
         "raag_uni":"ਰਾਗੁ ਆਸਾ",
         "raag_eng":"Raag Aasaa"
      },
      {
         "raag_id":9,
         "raag_uni":"ਰਾਗੁ ਗੂਜਰੀ",
         "raag_eng":"Raag Gujri"
      }
      ...
   ]

*Raags from Guru Granth Sahib Ji have Raag Ids from 5 to 35!*

Raag
^^^^

Get details of a specific Raag using Raag Id.

.. code:: python

   banidb.raag(raag_id)

**Parameters**:

-  **raag_id** *(int)* – id of the specific raag, recieved from the
   `raags <raags.html>`__ list.

**Returns**: Details of a specific Raag as list of dictionaries.

**Return type**: list of dict

**Example**:

.. code:: python

   raags_data = banidb.raag(8)
   print(raags_data)

**Output**

.. code:: 

   [
      {
         "raag_id": 8,
         "raag_uni": "ਰਾਗੁ ਆਸਾ",
         "raag": "Raag Aasaa",
         "time_of_raag": ("3:00","6:00"),
         "common_themes": "Hope",
         "feeling": "Determination",
         "angs": { "G":[347, 488] },
         "overview": "Aasaa has strong emotions of inspiration and courage. This Raag gives the listener the determination and ambition to put aside any excuses and to proceed with the necessary action to achieve the aim. It generates feelings of passion and zeal to succeed and the energy generated from these feelings enables the listener to find the strength from within to achieve success, even when the achievement seems difficult. The determined mood of this Raag ensures that failure is not an option and motivates the listener to be inspired.",
         "advanced":"Asa is a very old raga, once popular in the Punjab but seldom heard in concerts today. In the Ragmala this is a ragini of raga Megha. However, today it is assigned to the Bilaval thata.  Asa is a devotional raga for the cold season and is performed in the early morning just before sunrise. However, it is also known as a twilight melody with a calm mystical mood. Asa was used by Guru Nanak, Guru Angad, Guru Amar Das, Guru Ram Das, Guru Arjan and Guru Tegh Bahadur.In the Gurmat Sangeet style Aasa in a very important raag. The melodius notes of raag Asa are heard in every particle of the sacred land of Punjab. The golden rays of every dawn enter with the melodius tune of this raag and the redness of every dusk when it hides in the lap of nature, the melodious tunes of this raag sing the praises “Balhaaree kudarath vasiaa”.\nAsa raga literally means the melody of hope. As the Gurus emphasised the singing of God’s praises before dawn, this raga is conducive to kirtan before day-break. It is a soothing and pleasing raga, appropriate for the singing of the Asa-di-var, the morning-prayer of the Sikhs.",
         "musical_composure": "Aasa Raag literally means the melody of hope. This raag is conducive to the hours before day break and also around dusk. It is a soothing and pleasing raag, appropriate for the singing of the Aasa-di-vaar. This raag is considered to be an original musical gift from Guru Nanak as there is no mention of this raag in ancient or medieval texts. Guru Nanak, Guru Angad, Guru Amar Das, Guru Ram Das, Guru Arjun and Guru Tegh Bahadur have all recited Bani in this raag. Singing time of this raag is the fourth quarter of the night 3am to 6am. In the Sikh tradition this raag is also sung in the evening.",
         "placement": "First shabad titled 'Solar' has no rahau verse,\n\nAll other shabads and ashtpadis (pages 348 - 431 have rahau verses in them, placed mostly after the first padas, but also placed in the beginning of the shabad aswell (page 365);\n\nIn specialist compositions both 'Pattis' of Guru Nanak and Guru Amardas have one rahau verse each placed after the first padas\n\nAll shabads of the Bhagats have one rahau verse in them placed after the first padas of the shabads.\n",
         "aroh": "Sa, Re Ma, Pa, Dha Saˆˆ",
         "avroh": "Saˆˆ Nee Dha Pa, Ma, Ga Re Sa Re Ga Sa\n",
         "vadi": "Madhym (Ma)\n",
         "samvadi": "Sharaj (Sa)\n",
         "sur": "Gandhar and Nishad are forbidden notes in ascending scale, rest of the notes (swar) are sharp.\n",
         "thaat": "Bilawal",
         "jaati": "Aurav – Sampooran",
         "writers": [
            "Guru Nanak Dev Ji",
            "Guru Angad Dev Ji",
            "Guru Amar Daas Ji",
            "Guru Raam Daas Ji",
            "Guru Arjan Dev Ji",
            "Bhagat Dhannaa Ji",
            "Bhagat Kabeer Ji",
            "Bhagat Naam Dev Ji",
            "Bhagat Ravi Daas Ji",
            "Bhagat Dhannaa Ji"
         ]
      }
   ]

*Raags from Guru Granth Sahib Ji have Raag Ids from 5 to 35!*
