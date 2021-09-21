# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Print Check - BBL",
    "version": "14.0.1.0.0",
    "author": "Ecosoft",
    "summary": "Printing Check - BBL",
    "license": "AGPL-3",
    "depends": [
        "account_check_date",
        "account_check_payee",
        "account_check_printing_report_base",
        "l10n_th_amount_to_text",
        "l10n_th_fonts",
    ],
    "data": [
        "data/account_payment_check_report_data.xml",
        "data/report_data.xml",
        "report/report_check_bbl_base.xml",
    ],
    "installable": True,
    "maintainers": ["kittiu"],
}
