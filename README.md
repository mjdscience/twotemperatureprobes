# twotemperatureprobes
This programs takes information from multiple DS18B20 probes and posts their readings to Google Sheets using gspread.

The [tempReader](../blob/master/tempReader.py) program is sort of a base level program.  It returns elapsed time, and temperature values for each probe in the terminal.  It is a good place to start if you are just making sure that you are getting times and temperatures correctly.

The [tempLoggerGoogle](https://github.com/mjdscience/twotemperatureprobes/blob/master/tempLoggerGoogle "tempLoggerGoogle") program is a little more advanced.  It requires you to use the Google Cloud Platform in order to get the temperatuer readings in a sheet.  While it does require more work, you are able to log your data into something that is permanent and accessible from anywhere in the world.  I would recommend looking at this [GSpread tutorial](https://github.com/burnash/gspread), and this [datalogging tutorial](http://faradaysclub.com/?p=1556) before working with this.


