# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería, S.L.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "VAT in leads",
    "summary": "Add VAT field to leads",
    "version": "8.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "https://odoo-community.org/",
    "author": "Antiun Ingeniería S.L., "
              "AvanzOSC, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "contributors": [
        "Rafael Blasco <rafaelbn@antiun.com>",
        "Jairo Llopis <yajo.sk8@gmail.com>",
        "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
        "Ana Juaristi <anajuaristi@avanzosc.es>",
        "Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>",
        "Esther Martín <esthermartin@avanzosc.es>",
    ],
    "application": False,
    "installable": True,
    "depends": [
        "crm",
    ],
    "data": [
        "views/crm_lead.xml",
    ],
}
