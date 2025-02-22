"""The no quantization config"""
import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class NoQuantize:  # pylint: disable=too-many-instance-attributes
    """Configuration for no quantization"""

    name: str
    kind: str
    model_dtype: str  # "float16", "float32"

    def __post_init__(self):
        assert self.kind == "no-quant"
