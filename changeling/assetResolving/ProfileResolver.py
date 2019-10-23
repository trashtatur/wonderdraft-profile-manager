import logging
import os

import yaml

from changeling.pathfinder import Pathfinder


class ProfileResolver:

    def resolve_profile(self, profilename):
        profilename_cleaned = os.path.splitext(profilename)[0]
        profile_yml = self.__open_profile_by_name(profilename_cleaned)
        return profile_yml['modules']


    def __open_profile_by_name(self, profilename: str):

        try:
            with open(os.path.join(Pathfinder.get_profile_directory(), profilename + '.yml')) as profile:
                try:
                    return yaml.safe_load(profile)
                except yaml.YAMLError as exception:
                    logging.getLogger('debug').exception("YAML File seems to be tampered. Have you changed keys?")
        except OSError as exception:
            logging.getLogger('debug').exception(
                'Profile could not be opened. Was it the right name? Does it exist?')

