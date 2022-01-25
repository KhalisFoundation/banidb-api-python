Angs
----

Get Angs from specified `Source <sources.html>`__ using its corresponding
Ang Number(s)

.. code:: python

   banidb.angs(ang_no, source_id='G', larivaar=False, steek=False, translit=False)

You can specify Ang ranges in Ang_No as follows:

-  **ang_no='4-6'** gives angs 4,5,6 (from 4 to 6).
-  **ang_no='13+1313'** gives angs 13 and 1313.

The similar logic can used as **ang_no='4-6+13-15+1313'** which gives
angs 4, 5, 6, 13, 14, 15, 1313.

**Parameters:**

-  **ang_no** *(str or int)*: number of the specific ang.
-  `source_id <sources.html>`__ *(str)*: from where you want to the ang (by
   default, **G** for Guru Granth Sahib Ji).
-  **larivaar** *(bool)*: you want it to be in larivaar or not.
-  **steek** *(bool)*: you want steek (translations) or not.
-  **translit** *(bool)*: you want translitrations or not.

**Returns**: Search Results as dictionary(key-value pair).

**Return type**: dict

Example
^^^^^^^

.. code:: python

   # Searching Bandhana Har Bandhana Gun Gaavo Gopal Rai....
   ang_data = banidb.angs(1)
   print(ang_data)

**Output**

.. code:: 

   {
      "source":{
         "source_id":"G",
         "unicode":"ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ",
         "english":"Sri Guru Granth Sahib Ji",
         "ang_no":1
      },
      "page":[
         {
            "verse_id":1,
            "shabad_id":1,
            "verse":"ੴ ਸਤਿ ਨਾਮੁ ਕਰਤਾ ਪੁਰਖੁ ਨਿਰਭਉ ਨਿਰਵੈਰੁ ਅਕਾਲ ਮੂਰਤਿ ਅਜੂਨੀ ਸੈਭੰ ਗੁਰ ਪ੍ਰਸਾਦਿ ॥"
         },
         {
            "verse_id":2,
            "shabad_id":1,
            "verse":"॥ ਜਪੁ ॥"
         },
         {
            "verse_id":3,
            "shabad_id":1,
            "verse":"ਆਦਿ ਸਚੁ ਜੁਗਾਦਿ ਸਚੁ ॥"
         },
         {
            "verse_id":4,
            "shabad_id":1,
            "verse":"ਹੈ ਭੀ ਸਚੁ ਨਾਨਕ ਹੋਸੀ ਭੀ ਸਚੁ ॥੧॥"
         },
         {
            "verse_id":5,
            "shabad_id":1,
            "verse":"ਸੋਚੈ ਸੋਚਿ ਨ ਹੋਵਈ ਜੇ ਸੋਚੀ ਲਖ ਵਾਰ ॥"
         },
         {
            "verse_id":6,
            "shabad_id":1,
            "verse":"ਚੁਪੈ ਚੁਪ ਨ ਹੋਵਈ ਜੇ ਲਾਇ ਰਹਾ ਲਿਵ ਤਾਰ ॥"
         },
         {
            "verse_id":7,
            "shabad_id":1,
            "verse":"ਭੁਖਿਆ ਭੁਖ ਨ ਉਤਰੀ ਜੇ ਬੰਨਾ ਪੁਰੀਆ ਭਾਰ ॥"
         },
         {
            "verse_id":8,
            "shabad_id":1,
            "verse":"ਸਹਸ ਸਿਆਣਪਾ ਲਖ ਹੋਹਿ ਤ ਇਕ ਨ ਚਲੈ ਨਾਲਿ ॥"
         },
         {
            "verse_id":9,
            "shabad_id":1,
            "verse":"ਕਿਵ ਸਚਿਆਰਾ ਹੋਈਐ ਕਿਵ ਕੂੜੈ ਤੁਟੈ ਪਾਲਿ ॥"
         },
         {
            "verse_id":10,
            "shabad_id":1,
            "verse":"ਹੁਕਮਿ ਰਜਾਈ ਚਲਣਾ ਨਾਨਕ ਲਿਖਿਆ ਨਾਲਿ ॥੧॥"
         },
         {
            "verse_id":11,
            "shabad_id":2,
            "verse":"ਹੁਕਮੀ ਹੋਵਨਿ ਆਕਾਰ ਹੁਕਮੁ ਨ ਕਹਿਆ ਜਾਈ ॥"
         },
         {
            "verse_id":12,
            "shabad_id":2,
            "verse":"ਹੁਕਮੀ ਹੋਵਨਿ ਜੀਅ ਹੁਕਮਿ ਮਿਲੈ ਵਡਿਆਈ ॥"
         },
         {
            "verse_id":13,
            "shabad_id":2,
            "verse":"ਹੁਕਮੀ ਉਤਮੁ ਨੀਚੁ ਹੁਕਮਿ ਲਿਖਿ ਦੁਖ ਸੁਖ ਪਾਈਅਹਿ ॥"
         },
         {
            "verse_id":14,
            "shabad_id":2,
            "verse":"ਇਕਨਾ ਹੁਕਮੀ ਬਖਸੀਸ ਇਕਿ ਹੁਕਮੀ ਸਦਾ ਭਵਾਈਅਹਿ ॥"
         },
         {
            "verse_id":15,
            "shabad_id":2,
            "verse":"ਹੁਕਮੈ ਅੰਦਰਿ ਸਭੁ ਕੋ ਬਾਹਰਿ ਹੁਕਮ ਨ ਕੋਇ ॥"
         },
         {
            "verse_id":16,
            "shabad_id":2,
            "verse":"ਨਾਨਕ ਹੁਕਮੈ ਜੇ ਬੁਝੈ ਤ ਹਉਮੈ ਕਹੈ ਨ ਕੋਇ ॥੨॥"
         },
         {
            "verse_id":17,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਤਾਣੁ ਹੋਵੈ ਕਿਸੈ ਤਾਣੁ ॥"
         },
         {
            "verse_id":18,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਦਾਤਿ ਜਾਣੈ ਨੀਸਾਣੁ ॥"
         },
         {
            "verse_id":19,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਗੁਣ ਵਡਿਆਈਆ ਚਾਰ ॥"
         },
         {
            "verse_id":20,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਵਿਦਿਆ ਵਿਖਮੁ ਵੀਚਾਰੁ ॥"
         },
         {
            "verse_id":21,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਸਾਜਿ ਕਰੇ ਤਨੁ ਖੇਹ ॥"
         },
         {
            "verse_id":22,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਜੀਅ ਲੈ ਫਿਰਿ ਦੇਹ ॥"
         },
         {
            "verse_id":23,
            "shabad_id":3,
            "verse":"ਗਾਵੈ ਕੋ ਜਾਪੈ ਦਿਸੈ ਦੂਰਿ ॥"
         }
      ]
   }
