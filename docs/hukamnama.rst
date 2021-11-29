Hukamnama
---------

| Get Hukamnama Sahib of any specified date after 01/01/2002
| When no parameters are provided, it automatically gives the Hukamnama Sahib of current date, according to the availability and your Time Zone.

.. code:: python

    # Get Hukamnama for a specific date 
    data = banidb.hukamnama(year, month, day)
    print(data)

| **Output**
| The hukamnama sahib data can be accessed as follows:

.. code:: python

     {
         'hukam':[...] # List of all shabads(if more than one) in shabad format.
     }

`Shabad <shabad.html>`__ format
