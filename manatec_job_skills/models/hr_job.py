# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HrJob(models.Model):
    _inherit = 'hr.job'

    job_skill_ids = fields.One2many('hr.job.skill', 'job_id', string="Skills")
