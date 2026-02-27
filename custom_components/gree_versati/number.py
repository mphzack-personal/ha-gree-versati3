"""Number platform for Gree Versati."""

from __future__ import annotations

from homeassistant.components.number import NumberEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .client import GreeVersatiProtocolClient
from .constants import (
    CONF_DEVICE_ID,
    DATA_CLIENT,
    DATA_COORDINATOR,
    DATA_ENTRIES,
    HE_WAT_OUT_TEMP_SET_STEP,
    MAX_HE_WAT_OUT_TEMP_SET,
    MIN_HE_WAT_OUT_TEMP_SET,
    PARAM_HE_WAT_OUT_TEM_SET,
)
from .coordinator import GreeVersatiCoordinator
from .entity import GreeVersatiEntity


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up number entities."""
    runtime_data = hass.data[entry.domain][DATA_ENTRIES][entry.entry_id]
    async_add_entities(
        [
            GreeVersatiOutletSetpointNumber(
                runtime_data[DATA_COORDINATOR],
                entry.data[CONF_DEVICE_ID],
                runtime_data[DATA_CLIENT],
            )
        ]
    )


class GreeVersatiOutletSetpointNumber(GreeVersatiEntity, NumberEntity):
    """Number entity for heating water outlet setpoint."""

    _attr_translation_key = "he_wat_out_tem_set"
    _attr_native_unit_of_measurement = UnitOfTemperature.CELSIUS
    _attr_native_min_value = MIN_HE_WAT_OUT_TEMP_SET
    _attr_native_max_value = MAX_HE_WAT_OUT_TEMP_SET
    _attr_native_step = HE_WAT_OUT_TEMP_SET_STEP
    _attr_mode = "box"

    def __init__(
        self,
        coordinator: GreeVersatiCoordinator,
        device_id: str,
        client: GreeVersatiProtocolClient,
    ) -> None:
        super().__init__(coordinator, device_id, PARAM_HE_WAT_OUT_TEM_SET)
        self._client = client

    @property
    def native_value(self) -> float | None:
        """Return current setpoint value."""
        value = (self.coordinator.data or {}).get(PARAM_HE_WAT_OUT_TEM_SET)
        if value is None:
            return None
        try:
            return float(value)
        except (TypeError, ValueError):
            return None

    async def async_set_native_value(self, value: float) -> None:
        """Set water outlet setpoint."""
        await self._client.async_set({PARAM_HE_WAT_OUT_TEM_SET: int(round(value))})
        await self.coordinator.async_request_refresh()
