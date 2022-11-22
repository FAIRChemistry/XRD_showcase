import sdRDM

from typing import Optional
from typing import Optional, Union
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
        xml="@id",
    )

    name_exp: Optional[str] = Field(
        description="Name of the experimentator.", default=None
    )

    date: Optional[datetime] = Field(
        description="Date when the sample was measured.", default=None
    )

    compound: Optional[str] = Field(description="Name of the compound.", default=None)

    sample_id: Optional[str] = Field(
        description="ID of the measured sample", default=None
    )

    spec_inf: Optional[SpecInf] = Field(
        description="Information about the spectrometer.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/FAIRChemistry/XRD_showcase.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="3c73978ba7313281e1bee2de165e582fb355b4be"
    )
