Odoo keyword library for Robot Framework
========================================

**NOTE: This fork is a re-packaging of the BrainTec work by Akretion to make it easier to use. It also incorporate stuff from Kmee to avoid depening on erppeek**

It allows to play back Odoo browser based acceptance tests that are

* either written manually according to http://robotframework.org and this keyword library
* either recorded with modified Selenium plugin https://github.com/brain-tec/se-builder

Installation
============

.. code-block:: bash

  sudo pip install git+https://github.com/akretion/odoo-robot-framework.git


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


Results
=======

use the process return status and see detailed results in the generated report.html. Logs will be found in output.xml and log.html.