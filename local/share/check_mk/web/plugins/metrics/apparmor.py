#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import (
    metric_info,
    graph_info,
)


metric_info["apparmor_profiles_oaded"] = {
    "title": _("Profiles loaded"),
    "unit": "count",
    "color": "11/a",
}
metric_info["apparmor_profiles_enforced"] = {
    "title": _("Profiles enforced"),
    "unit": "count",
    "color": "21/a",
}
metric_info["apparmor_profiles_unconfined"] = {
    "title": _("Profiles unconfined"),
    "unit": "count",
    "color": "31/a",
}
metric_info["apparmor_profiles_complaining"] = {
    "title": _("Profiles complaining"),
    "unit": "count",
    "color": "41/a",
}
metric_info["apparmor_processes_enforced"] = {
    "title": _("Processes enforced"),
    "unit": "count",
    "color": "51/a",
}
metric_info["apparmor_processes_unconfined"] = {
    "title": _("Processes unconfined"),
    "unit": "count",
    "color": "61/a",
}
metric_info["apparmor_processes_complaining"] = {
    "title": _("Processes complaining"),
    "unit": "count",
    "color": "71/a",
}

graph_info["apparmor_profiles_combined"] = {
    "title": _("AppArmor profiles"),
    "metrics": [
        ("apparmor_profiles_oaded", "line"),
        ("apparmor_profiles_enforced", "line"),
        ("apparmor_profiles_unconfined", "line"),
        ("apparmor_profiles_complaining", "line"),
    ],
}

graph_info["apparmor_processes_combined"] = {
    "title": _("AppArmor processes"),
    "metrics": [
        ("apparmor_processes_enforced", "line"),
        ("apparmor_processes_unconfined", "line"),
        ("apparmor_processes_complaining", "line"),
    ],
}

