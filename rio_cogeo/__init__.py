"""rio_cogeo: Cloud Optimized GeoTIFF creation and validation plugin for rasterio."""

__version__ = "5.3.0"

from .cogeo import cog_info, cog_translate, cog_validate  # noqa
from .profiles import cog_profiles  # noqa
