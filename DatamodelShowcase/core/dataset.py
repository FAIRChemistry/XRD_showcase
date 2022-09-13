import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime

from .specinf import SpecInf


@forge_signature
class Dataset(sdRDM.DataModel):
    """..."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
    )

    compound: Optional[str] = Field(description="Name of the compound.", default=None)

    name_exp: Optional[str] = Field(
        description="Name of the experimentator.", default=None
    )

    date: Optional[str] = Field(
        description="Date when the sample was measured.", default=None
    )

    sample_id: Optional[str] = Field(
        description="ID of the measured sample", default=None
    )

    spec_inf: Optional[SpecInf] = Field(
        description="Information about the spectrometer.", default_factory=SpecInf
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/example_showcase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="8616086697bd98fa32c63145943156e8935b007c"
    )
