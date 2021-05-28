# Copyright 2018-2020 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_columns(
        env.cr, {'res_partner': [('zone_id', None), ('zone_group_id', None)]})
    openupgrade.remove_tables_fks(env.cr, ['res_better_zip_zone'])
    openupgrade.remove_tables_fks(env.cr, ['res_better_zip_zone_groups'])
