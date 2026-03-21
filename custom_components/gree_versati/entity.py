"""Base entity helpers for Gree Versati entities."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .constants import DOMAIN
from .coordinator import GreeVersatiCoordinator


class GreeVersatiEntity(CoordinatorEntity[GreeVersatiCoordinator]):
    """Base entity for Gree Versati integration."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: GreeVersatiCoordinator,
        device_id: str,
        param_key: str,
        unique_id_key: str | None = None,
    ) -> None:
        super().__init__(coordinator)
        self._device_id = device_id
        self._param_key = param_key
        self._attr_unique_id = f"{device_id}_{unique_id_key or param_key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device_id)},
            name=f"Gree Versati {device_id}",
            manufacturer="Gree",
            model="Versati 3",
        )
        self._optimistic_value: object = None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        data = self.coordinator.data or {}
        return super().available and self._param_key in data

    def _handle_coordinator_update(self) -> None:
        """Handle coordinator update - clear optimistic value."""
        self._optimistic_value = None
        super()._handle_coordinator_update()

    def _set_optimistic_value(self, value: object) -> None:
        """Set optimistic value and trigger UI update."""
        self._optimistic_value = value
        self.async_write_ha_state()
