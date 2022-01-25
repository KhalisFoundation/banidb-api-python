Kosh
----

Get words from Shabad Kosh starting with the given first letter, words
can be searched for meaning using `Kosh Word <#kosh-word>`__ function.

.. code:: python

   banidb.kosh(letter)

Returns words(starting with given letter).

**Parameters:**

-  **letter** *(str)*: the first letter of the words you wanna know.

**Returns**: Words (starting with letter) from kosh as list of
dictionaries.

**Return type**: list

**Example**:

.. code:: python

   kosh_data = banidb.kosh('d')
   print(kosh_data)

**Output**

.. code:: 

   [
       {
           "word_uni": "ਦ",
           "word": "d"
       },
       {
           "word_uni": "ਦਉਣੁ",
           "word": "dauxu"
       },
       {
           "word_uni": "ਦਉਤ",
           "word": "dauq"
       },
       {
           "word_uni": "ਦਉਰ",
           "word": "daur"
       }
   ]

Kosh Search
^^^^^^^^^^^

Get words and definitions related to query from Shabad Kosh.

.. code:: python

   banidb.kosh_search(query)

Returns related words with definition of given query word.

**Parameters:**

-  **query** *(str)*: the word whose related definitions you wanna know.

**Returns**: Related Definition of Words from Shabad Kosh as list of
dictionaries.

**Return type**: list

**Example**:

.. code:: python

   kosh_data = banidb.kosh_search('AnMd')
   print(kosh_data)

**Output**

.. code:: 

   [
       {
          "word_uni":"ਉਪਾਰਜਨਾ",
          "word":"aupwrjnw",
          "def_uni":"ਸੰ. ਉਪਰਾਗਨ. ਕ੍ਰਿ- ਰੰਗਣਾ. ਚਿਤ੍ਰਨਾ। ੨. ਸਿੰਗਾਰਨਾ. ""ਕੋਟਿ ਉਪਾਰਜਨਾ ਤੇਰੇ ਅੰਗ."" (ਭੈਰ ਅਃ ਮਃ ੫) ੩. ਸੰ. ਉਪਾਜੰਨ. ਜਮਾ ਕਰਨਾ. ""ਫਲਗੁਣਿ ਅਨੰਦ ਉਪਾਰਜਨਾ."" (ਮਾਝ ਬਾਰਾਮਾਹਾ) ੪. ਉਪਾਰ੍‌ਜਿਤ. ਪੈਦਾ ਕੀਤੀ ਹੋਈ- ਸ੍ਰਿਸ੍ਟੀ;. ਮਖ਼ਲੂਕ਼ਾਤ. ""ਸਿਮਰੈ ਸਗਲ ਉਪਾਰਜਨਾ."" (ਮਾਰੂ ਸੋਲਹੇ ਮਃ ੫) ""ਜੇਤ ਕੀਨ ਉਪਾਰਜਨਾ ਪ੍ਰਭੁ ਦਾਨ ਦੇਇ ਦਤਾਰ."" (ਮਾਲੀ ਮਃ ੫)"
          "def":"sM. auprwgn. ikR- rMgxw. icqRnw[ 2. isMgwrnw. ""koit aupwrjnw qyry AMg."" (BYr AÚ mÚ 5) 3. sM. aupwjMn. jmw krnw. ""Plguix AnMd aupwrjnw."" (mwJ bwrwmwhw) 4. aupwrijq. pYdw kIqI hoeI- isRs†I;. m^lUkæwq. ""ismrY sgl aupwrjnw."" (mwrU solhy mÚ 5) ""jyq kIn aupwrjnw pRBu dwn dyie dqwr."" (mwlI mÚ 5)",
       },
       {
          "word_uni":"ਅਸ਼੍ਰੁ",
          "word":"ASRü",
          "def_uni":"ਸੰ. ਸੰਗ੍ਯਾ- ਅੱਥਰੂ. ਆਂਸੂ. ਹੰਝੂ. ਸ਼ੋਕ ਜਾਂ ਅਨੰਦ ਦੇ ਅਸਰ ਨਾਲ ਨੇਤ੍ਰਾਂ ਤੋਂ ਨਿਕਲਿਆ ਜਲ."
          "def":"sM. sMgÎw- A`QrU. AWsU. hMJU. Sok jW AnMd dy Asr nwl nyqRW qoN inkilAw jl.",
       },
       {
          "word_uni":"ਅਕਥ",
          "word":"AkQ",
          "def_uni":"ਸੰ. ਅਕਥ੍ਯ. ਵਿ- ਜੋ ਬਿਆਨ ਨਾ ਕੀਤਾ ਜਾ ਸਕੇ. ਅਕਥਨੀਯ। ੨. ਪਾਰਬ੍ਰਹਮ. ਕਰਤਾਰ. ""ਅਕਥ ਕੀ ਕਰਹਿ ਕਹਾਣੀ."" (ਅਨੰਦੁ)"
          "def":"sM. AkQÎ. iv- jo ibAwn nw kIqw jw sky. AkQnIX[ 2. pwrbRhm. krqwr. ""AkQ kI krih khwxI."" (AnMdu)",
       }
       ...
   ]

Kosh Word
^^^^^^^^^

Get definition of given word from Shabad Kosh.

.. code:: python

   banidb.kosh_word(word)

Returns definition of given word.

**Parameters:**

-  **word** *(str)*: the word whose definition you wanna know.

**Returns**: Definition of Word from Shabad Kosh as list of
dictionaries.

**Return type**: list

**Example**:

.. code:: python

   kosh_data = banidb.kosh_word('d')
   print(kosh_data)

**Output**

.. code:: 

   [
      {
         "word_uni":"ਦ",
         "word":"d",
         "def_uni":"ਪੰਜਾਬੀ ਵਰਣਮਾਲਾ ਦਾ ਤੇਈਸਵਾਂ ਅੱਖਰ, ਇਸ ਦਾ ਉੱਚਾਰਣ ਅਸਥਾਨ ਦੰਦ ਹਨ. ਜੀਭ ਦੀ ਨੋਕ ਉੱਪਰਲੇ ਦੰਦਾਂ ਦੇ ਮੂਲ ਵਿੱਚ ਲੱਗਣ ਤੋਂ ਇਸ ਦਾ ਸ਼ਬਦ ਸਪਸ੍ਟ\uf032 ਹੁੰਦਾ ਹੈ। ੨. ਸੰ. ਸੰਗ੍ਯਾ- ਪਹਾੜ। ੩. ਦੰਦ. ਦਾਂਤ। ੪. ਰਖ੍ਯਾ. ਹਿਫ਼ਾਜ\uf033ਤ। ੫. ਭਾਰਯਾ. ਵਹੁਟੀ। ੬. ਵਿ- ਦਾਤਾ. ਦੇਣ ਵਾਲਾ. ਇਸ ਅਰਥ ਵਿੱਚ ਇਹ ਕਿਸੇ ਸ਼ਬਦ ਦੇ ਅੰਤ ਲੱਗਕੇ ਅਰਥ ਬੋਧ ਕਰਾਉਂਦਾ ਹੈ, ਜਿਵੇਂ- ਸੁਖਦ, ਜਲਦ ਆਦਿ.",
         "def":"pMjwbI vrxmwlw dw qyeIsvW A`Kr, ies dw au`cwrx AsQwn dMd hn. jIB dI nok au`prly dMdW dy mUl iv`c l`gx qoN ies dw Sbd sps†\uf032 huMdw hY[ 2. sM. sMgÎw- phwV[ 3. dMd. dWq[ 4. rKÎw. ih&wj\uf033q[ 5. BwrXw. vhutI[ 6. iv- dwqw. dyx vwlw. ies ArQ iv`c ieh iksy Sbd dy AMq l`gky ArQ boD krwauNdw hY, ijvyN- suKd, jld Awid."
      }
   ]
