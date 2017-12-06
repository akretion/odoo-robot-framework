Odoo keyword library for Robot Framework
========================================

**NOTE: This fork is a re-packaging of the BrainTec work by Akretion to make it easier to use. It also incorporates stuff from Kmee to avoid depending on the unmaintained erppeek**

It allows to play back Odoo browser based acceptance tests that are

* either written manually according to http://robotframework.org and this keyword library
* either recorded with modified Selenium plugin https://github.com/brain-tec/selenium-builder

Installation
============

.. code-block:: bash

  sudo pip install git+https://github.com/akretion/odoo-robot-framework.git

Also download Geckodriver (Firefox for Selenium) from https://github.com/mozilla/geckodriver/releases
This is **very important**: in same process or shell where you will be running the tests next, export a new PATH
that will include the geckodriver executable. For instance with if you put geckdriver in the same
directory where you will be running the tests (you shouldn't, it is just for the example):

.. code-block:: bash

  export PATH=$PATH:.

If you want to record tests with Selenium, there is a modified plugin version for Odoo.
In fact, there is a legacy Selenium plugin called se-builder and a new Selenium plugin called selenium-builder
and for each version there is a modified BrainTec fork. However it seems that for Odoo 8.0 at least only
the old se-builder plugin works. I'm not sure what is the correct one for the newest Odoo versions.

To install the modified Selenium Builder plugin for Firefox, on Ubuntu you would typically do

.. code-block:: bash

  git clone https://github.com/brain-tec/se-builder.git
  PROFILE=$(cat ~/.mozilla/firefox/profiles.ini | grep Path | tr "=" "\n" | tail -n1)
  cp -r se-builder/seleniumbuilder ~/.mozilla/firefox/$PROFILE/extensions/seleniumbuilder@saucelabs.com

If you use the selenium-builder newer plugin instead (incompatible with Odoo 8.0), it should be instead:

.. code-block:: bash

  git clone https://github.com/brain-tec/selenium-builder.git
  PROFILE=$(cat ~/.mozilla/firefox/profiles.ini | grep Path | tr "=" "\n" | tail -n1)
  cp -r se-builder/seleniumbuilder ~/.mozilla/firefox/$PROFILE/extensions/seleniumbuilder@sebuilder.com

Then restart Firefox (starting it from the terminal will help you to troubleshoot issues), ensure the add-on is enabled (possibly enable non signed addons in the settings).
Finally start the plugin with Tools>Web Developer>Launch Selenium Builder.

Usage
=====

Create a configuration config.py file such as:

.. code-block:: text

  # Time till the next command is executed
  SELENIUM_DELAY = 0

  # How long a "Wait Until ..." command should wait
  SELENIUM_TIMEOUT = 20
  BROWSER = "ff"
  Marionette= True

  # Odoo
  SERVER = "localhost"
  ODOO_PORT = "8069"
  ODOO_URL = "http://" + SERVER + ":" + ODOO_PORT
  ODOO_DB = "demo"
  USER = "admin"
  PASSWORD = "admin"

  # DB data
  ODOO_DB_USER = "alex"
  ODOO_DB_PASSWORD = "alex"
  ODOO_DB_PORT = "5432"


Create a testfile.robot file manually or using the Selenium recorder such as:

.. code-block:: text

  Resource       robotframework_odoo/odoo_8_0.robot

  Valid Login
    Login
  Creating a new quotation
    MainMenuText    Sales
    SubMenuText    Sales Orders
    Button	model=sale.order	button_name=oe_list_add
    Many2OneSelect    sale.order	partner_id	Agrolait
    NewOne2Many    sale.order	order_line
    Close Browser


Running tests
=============

.. code-block:: bash

  robot -v CONFIG:absolute_path_to_config.py testfile.robot

If this fails, read the html log file with your browser and ensure the the geckodriver executable is in your PATH.


Results
=======

use the process return status and see detailed results in the generated report.html. Logs will be found in output.xml and log.html.
