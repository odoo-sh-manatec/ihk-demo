# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class JobSkill(models.Model):
    _name = 'hr.job.skill'
    _description = "Skill level for a job"
    _rec_name = 'skill_id'
    _order = "skill_level_id"

    job_id = fields.Many2one('hr.job', required=True, ondelete='cascade')
    skill_id = fields.Many2one('hr.skill', required=True)
    skill_level_id = fields.Many2one('hr.skill.level', required=True)
    skill_type_id = fields.Many2one('hr.skill.type', required=True)
    level_progress = fields.Integer(related='skill_level_id.level_progress')

    _sql_constraints = [
        ('_unique_skill', 'unique (job_id, skill_id)', "Two levels for the same skill is not allowed"),
    ]

    @api.constrains('skill_id', 'skill_type_id')
    def _check_skill_type(self):
        for record in self:
            if record.skill_id not in record.skill_type_id.skill_ids:
                raise ValidationError(_("The skill %s and skill type %s doesn't match") % (record.skill_id.name, record.skill_type_id.name))

    @api.constrains('skill_type_id', 'skill_level_id')
    def _check_skill_level(self):
        for record in self:
            if record.skill_level_id not in record.skill_type_id.skill_level_ids:
                raise ValidationError(_("The skill level %s is not valid for skill type: %s ") % (record.skill_level_id.name, record.skill_type_id.name))


    employee_skill_ids = fields.One2many('hr.employee.skill', 'employee_id', string="Skills")