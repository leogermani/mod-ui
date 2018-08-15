# -*- coding: utf-8 -*-

#from mod.bank import list_banks, get_last_bank_and_pedalboard, save_last_bank_and_pedalboard


# The user profile models environmental context. That is all settings that
# are related to the physical hookup of the device. For example the
# MIDI control channels are related to an external controler, not to
# the saved banks, and they might change when the user moves.
class Profile:
    """User profile of environmental context."""

    name = "Default"
    
    # MIDI channels range in [0,15]
    # TODO: None when not used? Or -1?
    midi_prgch_bank_channel = 15
    midi_prgch_snapshot_channel = 14

    offer_bank_footswitch_navigation = False
    offer_snapshot_footswitch_navigation = False
    
    def set_midi_prgch_bank_channel(self, channel):
        result = False
        if 0 <= channel and channel < 16:
            if (channel != self.midi_prgch_snapshot_channel):
                midi_prgch_bank_channel = channel
                result = True                
        return result

    def set_midi_prgch_snapshot_channel(self, channel):
        result = False
        if 0 <= channel and channel < 16:
            if (channel != self.midi_prgch_bank_channel):
                midi_prgch_snapshot_channel = channel
                result = True
        return result