"""Constants for the Gree Versati integration."""

from __future__ import annotations

from typing import Final

from homeassistant.const import Platform

DOMAIN: Final = "gree_versati"

CONF_DEVICE_ID: Final = "device_id"
CONF_KEY: Final = "key"
CONF_TIMEOUT: Final = "timeout"
CONF_SCAN_INTERVAL: Final = "scan_interval"

DEFAULT_PORT: Final = 7000
DEFAULT_TIMEOUT: Final = 5
DEFAULT_SCAN_INTERVAL: Final = 30
DEFAULT_RETRIES: Final = 2

MIN_HE_WAT_OUT_TEMP_SET: Final = 20
MAX_HE_WAT_OUT_TEMP_SET: Final = 60
HE_WAT_OUT_TEMP_SET_STEP: Final = 1

MIN_WAT_BOX_TEMP_SET: Final = 20
MAX_WAT_BOX_TEMP_SET: Final = 60
WAT_BOX_TEMP_SET_STEP: Final = 1

PARAM_HE_WAT_OUT_TEM_SET: Final = "HeWatOutTemSet"
PARAM_WAT_BOX_TEM_SET: Final = "WatBoxTemSet"
PARAM_TEM_UN: Final = "TemUn"
PARAM_ALL_ERR: Final = "AllErr"
PARAM_MOD: Final = "Mod"
PARAM_POW: Final = "Pow"
PARAM_HEP_OUT_WAT_TEM_HI: Final = "HepOutWatTemHi"
PARAM_HEP_OUT_WAT_TEM_LO: Final = "HepOutWatTemLo"
PARAM_ALL_IN_WAT_TEM_HI: Final = "AllInWatTemHi"
PARAM_ALL_IN_WAT_TEM_LO: Final = "AllInWatTemLo"
PARAM_WAT_BOX_TEM_HI: Final = "WatBoxTemHi"
PARAM_WAT_BOX_TEM_LO: Final = "WatBoxTemLo"
PARAM_ALL_OUT_WAT_TEM_HI: Final = "AllOutWatTemHi"
PARAM_ALL_OUT_WAT_TEM_LO: Final = "AllOutWatTemLo"
PARAM_RMO_HOM_TEM_HI: Final = "RmoHomTemHi"
PARAM_RMO_HOM_TEM_LO: Final = "RmoHomTemLo"

POLL_KEYS: Final[tuple[str, ...]] = (
    PARAM_HE_WAT_OUT_TEM_SET,
    PARAM_WAT_BOX_TEM_SET,
    PARAM_TEM_UN,
    PARAM_ALL_ERR,
    PARAM_MOD,
    PARAM_POW,
    PARAM_HEP_OUT_WAT_TEM_HI,
    PARAM_HEP_OUT_WAT_TEM_LO,
    PARAM_ALL_IN_WAT_TEM_HI,
    PARAM_ALL_IN_WAT_TEM_LO,
    PARAM_WAT_BOX_TEM_HI,
    PARAM_WAT_BOX_TEM_LO,
    PARAM_ALL_OUT_WAT_TEM_HI,
    PARAM_ALL_OUT_WAT_TEM_LO,
    PARAM_RMO_HOM_TEM_HI,
    PARAM_RMO_HOM_TEM_LO,
)

SERVICE_SET_PARAM: Final = "set_param"
SERVICE_GET_PARAMS: Final = "get_params"

ATTR_KEY: Final = "key"
ATTR_KEYS: Final = "keys"
ATTR_VALUE: Final = "value"

DEFAULT_MAX_DATAGRAM_BYTES: Final = 8192

DATA_ENTRIES: Final = "entries"
DATA_CLIENT: Final = "client"
DATA_COORDINATOR: Final = "coordinator"

MODE_OPTIONS: Final[dict[str, int]] = {
    "Heat": 1,
    "Cool": 5,
    "Hot water": 2,
    "Cool + hot water": 3,
    "Heat + hot water": 4,
}

PLATFORMS: Final[list[Platform]] = [
    Platform.NUMBER,
    Platform.SENSOR,
    Platform.SWITCH,
    Platform.SELECT,
]
