from .agent_based_api.v1 import *
from datetime import datetime
import json

def discover_apparmor(section):
    yield Service()

def check_apparmor(params, section):
    profiles_enforced = 0
    profiles_complain = 0
    profiles_unconfined = 0
    profiles_loaded = 0
    processes_enforced = 0
    processes_complain = 0
    processes_unconfined = 0
    state = State.OK
    summary = "Unknown."

    # count profiles
    for name in section["profiles"]:
        profiles_loaded = profiles_loaded + 1
        if section["profiles"][name] == "enforce":
          profiles_enforced = profiles_enforced + 1
        elif section["profiles"][name] == "complain":
          profiles_complain = profiles_complain + 1
        elif section["profiles"][name] == "unconfined":
          profiles_unconfined = profiles_unconfined + 1

    # count processes
    for name in section["processes"]:
        for process in section["processes"][name]:
            if process["status"] == "enforce":
              processes_enforced = processes_enforced + 1
            elif process["status"] == "complain":
               processes_complain = processes_complain + 1
            elif process["status"] == "unconfined":
               processes_unconfined = processes_unconfined + 1


    # change state if neccessary 
    if profiles_complain >= int(params["profiles_complain"][0]):
      if profiles_complain >= int(params["profiles_complain"][1]):
        state = State.CRIT
      else:
        state = State.WARN
    if profiles_unconfined >= int(params["profiles_unconfined"][0]):
      if profiles_unconfined >= int(params["profiles_unconfined"][1]):
        state = State.CRIT
      else:
        state = State.WARN
    if processes_complain >= int(params["processes_complain"][0]):
      if processes_complain >= int(params["processes_complain"][1]):
        state = State.CRIT
      else:
        state = State.WARN
    if processes_unconfined >= int(params["processes_unconfined"][0]):
      if processes_unconfined >= int(params["processes_unconfined"][1]):
        state = State.CRIT
      else:
        state = State.WARN

    if state == State.WARN or state == State.CRIT:
        summary = "AppArmor not fully enforced."
    elif state == State.OK:
        summary = "AppArmor fully enforced."

    details = ("{} profiles are loaded.\n"
        "{} profiles are in enforce mode.\n"
        "{} profiles are in complain mode.\n"
        "{} profiles are unconfined.\n"
        "{} processes are in enforce mode.\n"
        "{} processes are in complain mode.\n"
        "{} processes are unconfined.").format(
        profiles_loaded,
        profiles_enforced,
        profiles_complain,
        profiles_unconfined,
        processes_enforced,
        processes_complain,
        processes_unconfined)

    yield Metric("apparmor_profiles_loaded", profiles_loaded)
    yield Metric("apparmor_profiles_enforced", profiles_enforced)
    yield Metric("apparmor_profiles_complaining", profiles_complain)
    yield Metric("apparmor_profiles_unconfined", profiles_unconfined)
    yield Metric("apparmor_processes_enforced", processes_enforced)
    yield Metric("apparmor_processes_complaining", processes_complain)
    yield Metric("apparmor_processes_unconfined", processes_unconfined)
    
    yield Result(state=state, summary=summary, details=details)

register.check_plugin(
    name = "apparmor",
    service_name = "AppArmor status",
    discovery_function = discover_apparmor,
    check_function = check_apparmor,
    check_default_parameters={
        "processes_complain": (1, 2),
        "processes_unconfined": (1, 2),
        "profiles_complain": (1, 2),
        "profiles_unconfined": (1, 2)
    },
    check_ruleset_name="apparmor",
)

def parse_apparmor(string_table):
    if len(string_table) > 0:
        line = str(" ".join(string_table[0]))
        json_dict = json.loads(line)
    return json_dict

register.agent_section(
    name = "apparmor",
    parse_function = parse_apparmor,
)

