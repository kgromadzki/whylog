from abc import ABCMeta, abstractmethod


class AbstractConfig(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_investigation_plan(self, front_input):
        pass


class YamlConfig(AbstractConfig):
    def __init__(self, parsers_path, rules_path, log_locations_path):
        pass

    def create_investigation_plan(self, front_input):
        pass

    def _get_log_type(self, front_input):
        pass

    def _find_matching_parsers(self, front_input, log_type):
        pass

    def _filter_rule_set(self, parsers_list):
        pass

    def _get_locations_for_logs(self, logs_types_list):
        pass


class InvestigationPlan(object):
    def __init__(self, front_input, rule_subset, log_location_dict):
        pass

    def get_next_investigation_step(self):
        pass


class RuleSubset(object):
    def get_logs_types(self):
        pass

    def get_rules_for_log_type(self, log_type):
        pass

    def get_parsers_for_log_type(self, log_type):
        pass


class InvestigationStep(object):
    def __init__(self, parsers, rules, log_location, front_input):
        pass

    def get_clues(self, line):
        pass


class AbstractParser(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_clue(self, line):
        pass


class RegexParser(AbstractParser):
    def __init__(self, name, regex, params):
        pass

    def get_clue(self, line):
        pass


class Rule(object):
    def __init__(self, causes, effect, constraints):
        pass


class LogType(object):
    def __init__(self, type_name):
        pass


class LogLocation(object):
    def __init__(self, filename_parser, log_type):
        pass


class AbstractFilenameParser(object):
    __metaclass__ = ABCMeta


class RegexFilenameParser(AbstractFilenameParser):
    def __init__(self, path_pattern):
        pass
