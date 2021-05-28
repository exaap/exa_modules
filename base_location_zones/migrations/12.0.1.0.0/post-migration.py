# Copyright 2021 Alejandro Olano <Github@alejo-code>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):

    openupgrade.logged_query(
        env.cr, """
        UPDATE res_city_zip_zone rbz
		SET name = rc.name
        FROM res_better_zip_zone rc
        WHERE rc.id = rbz.id""")

    openupgrade.logged_query(
        env.cr, """
        UPDATE res_city_zip_zone rbz
		SET zip_id = rc.zip_id
        FROM res_better_zip_zone rc
        WHERE rc.id = rbz.id""")

    openupgrade.logged_query(
        env.cr, """
        UPDATE res_city_zip_zone_groups rbz
		SET name = rc.name
        FROM res_better_zip_zone_groups rc
        WHERE rc.id = rbz.id""")
