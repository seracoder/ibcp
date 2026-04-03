
IBCP: Python Wrapper for Interactive Brokers API
================================================

.. image:: https://img.shields.io/pypi/v/ibcp
   :target: https://pypi.org/pypi/ibcp/
.. image:: https://img.shields.io/pypi/pyversions/ibcp
   :target: https://pypi.org/pypi/ibcp/
.. image:: https://img.shields.io/pypi/l/ibcp
   :target: https://pypi.org/pypi/ibcp/
.. image:: https://readthedocs.org/projects/ibcp/badge/?version=latest
   :target: https://ibcp.readthedocs.io/en/latest/?badge=latest

.. figure:: https://raw.githubusercontent.com/matthewmoorcroft/ibcp/main/docs/logo.png
   :alt: Logo for 'IBCP'
   :align: center

Overview
--------

|   IBCP is an unofficial python wrapper for `Interactive Brokers Client Portal Web API <https://interactivebrokers.github.io/cpwebapi/>`__. The motivation for the project was to build a Python wrapper
|   that is easy to use and understand.

Please see https://ibcp.readthedocs.io for the full documentation.

Features
--------

- Simple REST API wrapper
- Easy to use and understand
- Supports all Interactive Brokers Client Portal Web API endpoints
- Handles authentication and session management
- Supports both SSL and non-SSL connections

Requirements
------------

IBCP assumes a gateway session is active and authenticated.

Installation
------------

IBCP was developed under the `Voyz/IBeam <https://github.com/voyz/ibeam>`__ docker image environment.

Once a gateway session is running, ``pip`` command can be used to install IBCP:

.. code-block:: bash

   pip install ibcp

Usage
--------

.. code-block:: python

   import asyncio
   import ibcp

   async def main():
       # default parameters: url="https://localhost:5000", ssl=False
       ib = ibcp.REST()
       await ib.set_default_account()

       # Get account information
       account = await ib.get_accounts()

       # Get portfolio
       portfolio = await ib.get_portfolio()

       # Get cash balance
       balance = await ib.get_cash_balance()

       # Get net value
       net_value = await ib.get_netvalue()

       # Get market data
       bars = await ib.get_bars("AAPL")

       # Get contract ID
       conid = await ib.get_conid("AAPL")

       # Place order
       orders = [
           {
               "conid": conid,
               "orderType": "MKT",
               "side": "BUY",
               "quantity": 100,
               "tif": "DAY",
           }
       ]
       result = await ib.submit_orders(orders)

       await ib.close()

   asyncio.run(main())

For the complete reference, please visit https://ibcp.readthedocs.io/en/latest/reference.html.

Configuration
-------------

By default, IBCP assumes the gateway session is open at https://localhost:5000 without an SSL certificate. A custom URL and SSL certificate can be set by:

.. code-block:: python

   async with ibcp.REST(url="https://localhost:5000", ssl=False) as ib:
       await ib.set_default_account()
       # ... async calls
       pass

Documentation of available functions is at https://ibcp.readthedocs.io/en/latest/reference.html.

