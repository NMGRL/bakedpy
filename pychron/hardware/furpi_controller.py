# ===============================================================================
# Copyright 2016 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= enthought library imports =======================
# ============= standard library imports ========================
# ============= local library imports  ==========================
from pychron.hardware.core.core_device import CoreDevice


class FurpiController(CoreDevice):
    def get_temp_and_power(self):
        return self.ask('GetTempAndPower')

    def get_temperature(self):
        return self.ask('GetTemperature')

    def is_programmed(self):
        return True

    def set_control_mode(self, mode):
        return self.ask('SetControlMode {}'.format(mode))

    def set_closed_loop_setpoint(self, setpoint):
        return self.ask('SetClosedLoopSetpoint {}'.format(setpoint))

    def set_ramp_scale(self, *args, **kw):
        pass

    def set_ramp_action(self, *args, **kw):
        pass

    def set_ramp_rate(self, *args, **kw):
        pass

# ============= EOF =============================================
