"""Sensor platform for Gree Versati."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .constants import (
    CONF_DEVICE_ID,
    DATA_COORDINATOR,
    DATA_ENTRIES,
    PARAM_ALL_ERR,
    PARAM_ALL_IN_WAT_TEM_HI,
    PARAM_ALL_IN_WAT_TEM_LO,
    PARAM_ALL_OUT_WAT_TEM_HI,
    PARAM_ALL_OUT_WAT_TEM_LO,
    PARAM_AN_FRZZ_RUN_STA,
    PARAM_ELC_HE1_RUN_STA,
    PARAM_ELC_HE2_RUN_STA,
    PARAM_HE_WAT_OUT_TEM_SET,
    PARAM_HEP_OUT_WAT_TEM_HI,
    PARAM_HEP_OUT_WAT_TEM_LO,
    PARAM_MOD,
    PARAM_POW,
    PARAM_RMO_HOM_TEM_HI,
    PARAM_RMO_HOM_TEM_LO,
    PARAM_SY_AN_FRO_RUN_STA,
    PARAM_TEM_UN,
    PARAM_HET_HT_WTER,
    PARAM_SV_ST,
    PARAM_WAT_BOX_ELC_HE_RUN_STA,
    PARAM_WAT_BOX_TEM_SET,
    PARAM_WAT_BOX_TEM_HI,
    PARAM_WAT_BOX_TEM_LO,
)
from .coordinator import GreeVersatiCoordinator
from .entity import GreeVersatiEntity


@dataclass(frozen=True, kw_only=True)
class GreeVersatiSensorDescription(SensorEntityDescription):
    """Description of a Gree Versati sensor."""

    param_key: str | None = None
    param_key_hi: str | None = None
    param_key_lo: str | None = None


SENSOR_DESCRIPTIONS: tuple[GreeVersatiSensorDescription, ...] = (
    GreeVersatiSensorDescription(
        key="he_wat_out_tem_set",
        translation_key="he_wat_out_tem_set",
        param_key=PARAM_HE_WAT_OUT_TEM_SET,
    ),
    GreeVersatiSensorDescription(
        key="wat_box_tem_set",
        translation_key="wat_box_tem_set",
        param_key=PARAM_WAT_BOX_TEM_SET,
    ),
    GreeVersatiSensorDescription(
        key="tem_un",
        translation_key="tem_un",
        param_key=PARAM_TEM_UN,
    ),
    GreeVersatiSensorDescription(
        key="all_err",
        translation_key="all_err",
        param_key=PARAM_ALL_ERR,
    ),
    GreeVersatiSensorDescription(
        key="mod",
        translation_key="mod",
        param_key=PARAM_MOD,
    ),
    GreeVersatiSensorDescription(
        key="pow",
        translation_key="pow",
        param_key=PARAM_POW,
    ),
    GreeVersatiSensorDescription(
        key="t_optional_water_sen",
        translation_key="t_optional_water_sen",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        param_key_hi=PARAM_HEP_OUT_WAT_TEM_HI,
        param_key_lo=PARAM_HEP_OUT_WAT_TEM_LO,
    ),
    GreeVersatiSensorDescription(
        key="t_water_in_pe",
        translation_key="t_water_in_pe",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        param_key_hi=PARAM_ALL_IN_WAT_TEM_HI,
        param_key_lo=PARAM_ALL_IN_WAT_TEM_LO,
    ),
    GreeVersatiSensorDescription(
        key="t_water_tank",
        translation_key="t_water_tank",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        param_key_hi=PARAM_WAT_BOX_TEM_HI,
        param_key_lo=PARAM_WAT_BOX_TEM_LO,
    ),
    GreeVersatiSensorDescription(
        key="t_water_out_pe",
        translation_key="t_water_out_pe",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        param_key_hi=PARAM_ALL_OUT_WAT_TEM_HI,
        param_key_lo=PARAM_ALL_OUT_WAT_TEM_LO,
    ),
    GreeVersatiSensorDescription(
        key="remote_room_temperature",
        translation_key="remote_room_temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        param_key_hi=PARAM_RMO_HOM_TEM_HI,
        param_key_lo=PARAM_RMO_HOM_TEM_LO,
    ),
    GreeVersatiSensorDescription(
        key="het_ht_wter",
        translation_key="het_ht_wter",
        param_key=PARAM_HET_HT_WTER,
    ),
    GreeVersatiSensorDescription(
        key="elc_he1_run_sta",
        translation_key="elc_he1_run_sta",
        param_key=PARAM_ELC_HE1_RUN_STA,
    ),
    GreeVersatiSensorDescription(
        key="elc_he2_run_sta",
        translation_key="elc_he2_run_sta",
        param_key=PARAM_ELC_HE2_RUN_STA,
    ),
    GreeVersatiSensorDescription(
        key="wat_box_elc_he_run_sta",
        translation_key="wat_box_elc_he_run_sta",
        param_key=PARAM_WAT_BOX_ELC_HE_RUN_STA,
    ),
    GreeVersatiSensorDescription(
        key="an_frzz_run_sta",
        translation_key="an_frzz_run_sta",
        param_key=PARAM_AN_FRZZ_RUN_STA,
    ),
    GreeVersatiSensorDescription(
        key="sy_an_fro_run_sta",
        translation_key="sy_an_fro_run_sta",
        param_key=PARAM_SY_AN_FRO_RUN_STA,
    ),
    GreeVersatiSensorDescription(
        key="sv_st",
        translation_key="sv_st",
        param_key=PARAM_SV_ST,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up sensors from a config entry."""
    runtime_data = hass.data[entry.domain][DATA_ENTRIES][entry.entry_id]
    coordinator = runtime_data[DATA_COORDINATOR]
    device_id = entry.data[CONF_DEVICE_ID]

    async_add_entities(
        GreeVersatiSensor(coordinator, device_id, description)
        for description in SENSOR_DESCRIPTIONS
    )


class GreeVersatiSensor(GreeVersatiEntity, SensorEntity):
    """Represents a generic value sensor from device parameters."""

    entity_description: GreeVersatiSensorDescription

    def __init__(
        self,
        coordinator: GreeVersatiCoordinator,
        device_id: str,
        description: GreeVersatiSensorDescription,
    ) -> None:
        param_key = description.param_key or description.param_key_hi or ""
        super().__init__(coordinator, device_id, param_key)
        self.entity_description = description

    @property
    def native_value(self) -> str | int | float | bool | None:
        """Return raw protocol value or calculated combined value."""
        data = self.coordinator.data or {}
        
        # Handle combined Hi/Lo temperature sensors
        if self.entity_description.param_key_hi and self.entity_description.param_key_lo:
            hi = data.get(self.entity_description.param_key_hi)
            lo = data.get(self.entity_description.param_key_lo)
            if hi is not None and lo is not None:
                return round((float(hi) - 100) + float(lo) / 10, 1)
            return None
        
        # Handle single value sensors
        return data.get(self.entity_description.param_key)
