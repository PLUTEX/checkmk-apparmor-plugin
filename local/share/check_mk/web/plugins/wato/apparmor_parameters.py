#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)
from cmk.gui.valuespec import Age, Dictionary, TextInput, Tuple


def _parameter_valuespec_apparmor():
    return Dictionary(
        elements=[
            (
                "processes_complain",
                Tuple(
                    title=_("Allowed number of processes in complain mode."),
                    elements=[
                        Integer(title=_("Warning if more than"), default_value=1),
                        Integer(title=_("Critical if more than"), default_value=2),
                    ],
                ),
            ),
            (
                "processes_unconfined",
                Tuple(
                    title=_("Allowed number of processes in unconfined mode."),
                    elements=[
                        Integer(title=_("Warning if more than"), default_value=1),
                        Integer(title=_("Critical if more than"), default_value=2),
                    ],
                ),
            ),
            (
                "profiles_complain",
                Tuple(
                    title=_("Allowed number of profiles in complain mode."),
                    elements=[
                        Integer(title=_("Warning if more than"), default_value=1),
                        Integer(title=_("Critical if more than"), default_value=2),
                    ],
                ),
            ),
            (
                "profiles_unconfined",
                Tuple(
                    title=_("Allowed number of profiles in unconfined mode."),
                    elements=[
                        Integer(title=_("Warning if more than"), default_value=1),
                        Integer(title=_("Critical if more than"), default_value=2),
                    ],
                ),
            )
        ],
    )


rulespec_registry.register(
    CheckParameterRulespecWithoutItem(
        check_group_name="apparmor",
        group=RulespecGroupCheckParametersApplications,
        match_type="dict",
        parameter_valuespec=_parameter_valuespec_apparmor,
        title=lambda: _("AppArmor"),
    )
)
