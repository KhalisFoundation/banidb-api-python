Rehats
------

Get all available Rehats with Rehat Ids.

.. code:: python

   banidb.rehats()

**Returns**: rehats with rehat ids to be used in other functions to read
specific rehats or chapter.

**Return type**: dict

**Example**:

.. code:: python

   rehats_data = banidb.rehats()
   print(rehats_data)

**Output**

.. code:: 

   [
      {
         "rehat_id":1,
         "rehat_name":"Sikh Rehat Maryada (Akal Takht Sahib)"
      },
      {
         "rehat_id":2,
         "rehat_name":"ਸਿੱਖ ਰਹਿਤ ਮਰਯਾਦਾ (ਅਕਾਲ ਤਖ਼ਤ ਸਾਹਿਬ)"
      },
      {
         "rehat_id":3,
         "rehat_name":"Gurmat Rehat Maryada (Damdami Taksal)"
      },
      {
         "rehat_id":4,
         "rehat_name":"Points of Contention (AKJ)"
      }
   ]

Rehat
^^^^^

Get all available Chapters Ids with names in the specific Rehat.

.. code:: python

   banidb.rehat(rehat_id)

**Parameters**:

-  **rehat_id** *(int)*: id of the specific rehat.

**Returns**: chapters ids with names of spefic rehat to be used in other
functions to read specific chapter.

**Return type**: dict

**Example**:

.. code:: python

   rehat_data = banidb.rehat(1)
   print(rehat_data)

**Output**:

.. code:: 

   {
      "rehat_id":1,
      "chapters":[
         {
            "chapter_id":1,
            "chapter_name":"Sikh Defined"
         },
         {
            "chapter_id":2,
            "chapter_name":"Aspects of Sikh Living"
         },
         {
            "chapter_id":3,
            "chapter_name":"Individual Spirituality"
         }
         ...
      ]
   }

Rehat Chapter
^^^^^^^^^^^^^

Get the data in the specific Chapter of a Rehat.

.. code:: python

   banidb.rehat_chapter(rehat_id, chapter_id)

**Parameters**:

-  **rehat_id** *(int)*: id of the specific rehat.
-  **chapter_id** *(int)*: id of the specific chapter.

**Returns**: content of a specific chapter of a rehat.

**Return type**: dict

**Example**:

.. code:: python

   rehat_data = banidb.rehat_chapter(1,1)
   print(rehat_data)

**Output**:

.. code:: 

   {
      "rehat_id":1,
      "chapter_id":1,
      "alphabet":"english",
      "content":"Article I\nAny human being who faithfully believes in\ni. One Immortal Being, \n ii. Ten Gurus, from Guru Nanak Sahib to Guru Gobind Singh Sahib,\niii. The Guru Granth Sahib, \niv. The utterances and teachings of the ten Gurus,\nv. The baptism bequeathed by the tenth Guru, and who does not owe allegiance to any\nother religion, is a Sikh."
   }

Rehat Search
^^^^^^^^^^^^

Get Chapter Id and Rehat Id of the content related to your query.

.. code:: python

   banidb.rehat_search(query)

**Parameters**:

-  **query** *(str)*: your query to be searched.

**Returns**: chapter id and rehat id of the content related to your
query .

**Return type**: list of dict

**Example**:

.. code:: python

   rehat_data = banidb.rehat_search('sikh')
   print(rehat_data)

**Output**:

.. code:: 

   [
      {
         "rehat_id":1,
         "rehat_name":"Sikh Rehat Maryada (Akal Takht Sahib)",
         "chapter_id":1,
         "chapter_name":"Sikh Defined"
      },
      {
         "rehat_id":1,
         "rehat_name":"Sikh Rehat Maryada (Akal Takht Sahib)",
         "chapter_id":2,
         "chapter_name":"Aspects of Sikh Living"
      },
      {
         "rehat_id":1,
         "rehat_name":"Sikh Rehat Maryada (Akal Takht Sahib)",
         "chapter_id":3,
         "chapter_name":"Individual Spirituality"
      }
      ...
   ]
