from ..devices.base import WinkDevice


class WinkGarageDoor(WinkDevice):
    """
    Represents a Wink garage door.
    """

    def state(self):
        return self._last_reading.get('position', 0)

    def tamper_detected(self):
        tamper = self._last_reading.get('tamper_detected_true', False)
        if tamper is None:
            tamper = False
        return tamper

    def set_state(self, state):
        """
        :param state:   a number of 1 ('open') or 0 ('close')
        :return: nothing
        """
        values = {"desired_state": {"position": state}}
        response = self.api_interface.set_device_state(self, values)
        self._update_state_from_response(response)
