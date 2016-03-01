from whylog.config.parsers import *
from abc import ABCMeta, abstractmethod
import yaml
import logging


class AbstractConfig(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_investigation_plan(self, front_input):
        pass


class YamlConfig(AbstractConfig):
    def __init__(self, parsers_path, rules_path, log_locations_path):
        self._parsers_path = parsers_path
        self._rules_path = rules_path
        self._log_locations_path = log_locations_path
        self._parsers = self._load_parsers()

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

    def _load_config_from_file(self, path):
        with open(path, "r") as config_file:
            return list(yaml.load_all(config_file))

    def _create_parser_object(self, document):
        if document.get("log_type") is None:
            log_type = LogType("default")
        else:
            log_type = LogType(document.get("log_type"))
        document["log_type"] = log_type
        if document.get("class") is None:
            if document.get("params") is None:
                document["params"] = []
            return RegexParser(**document)
        else:
            try:
                parser_class = globals()[document.get("class")]
                del document["class"]
                return parser_class(**document)
            except KeyError:
                logging.error("Unable to creating object of " + document.get("class") + " class")
                return None

    def _load_parsers(self):
        documents = self._load_config_from_file(self._parsers_path)
        parsers = []
        for document in documents:
            parser = self._create_parser_object(document)
            if parser is not None:
                parsers.append(parser)
        return parsers


class InvestigationPlan(object):
    def __init__(self, front_input, rule_subset, log_location_dict):
        pass

    def get_next_investigation_step(self):
        pass


class RuleSubset(object):
    def __init__(self, rule_dict):
        pass

    def get_logs_types(self):
        pass

    def get_rules_for_log_type(self, log_type):
        pass

    def get_parsers_for_log_type(self, log_type):
        pass


class InvestigationStep(object):
    """
    Represents rules, parsers and locations of logs which are necessary
    to find and parse log files with potential causes.
    """

    def __init__(self, parsers, rules, log_location, effect_time):
        pass

    def get_clues(self, line):
        """
        Basing on parsers creates clues in investigation
        :param line: line from parsed file
        :returns: list of created clues
        """
        pass


class Clue(object):
    """
    Collects all the data that parser can extract from single log line.
    Also, contains parsed line and its source.
    """

    def __init__(self, regex_parameters, line_time, line_content, line_source):
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
